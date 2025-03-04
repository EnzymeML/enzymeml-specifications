module EnzymeMLSystem

using Symbolics, DifferentialEquations, ModelingToolkit

"""
    define_variables(var_names)

Create symbolic variables for an ODE system that are functions of time.

# Arguments
- `var_names`: Vector of strings containing the names of variables to create

# Returns
- Dictionary mapping variable names to their symbolic representations
"""
function define_variables(var_names)
    @independent_variables t

    vars = Dict(name => (@variables $(Symbol(name))(t))[1] for name in var_names)

    return vars
end

"""
    define_parameters(param_names)

Create symbolic parameters for an ODE system.

# Arguments
- `param_names`: Vector of strings containing the names of parameters to create

# Returns
- Dictionary mapping parameter names to their symbolic representations
"""
function define_parameters(param_names)
    params = Dict(name => (@parameters $(Symbol(name)))[1] for name in param_names)
    return params
end

"""
    @system(enzmldoc::EnzymeMLDocument)

Create an ODE system directly from an EnzymeMLDocument.

# Arguments
- `enzmldoc`: An EnzymeMLDocument containing the model specification

# Returns
- Tuple containing:
  - The simplified ODE system
  - Dictionary of variable references
  - Dictionary of parameter references

# Example
```julia
enzmldoc = JSON3.read(json_string, EnzymeMLDocument)
sys, vars, params = @define_ode_problem(enzmldoc)
```
"""
macro system(enzmldoc::Symbol)
    quote
        let
            # Extract parameters and equations from document
            parameters = Dict(parameter.symbol => parameter for parameter in $(esc(enzmldoc)).parameters)
            param_symbols = collect(keys(parameters))
            equations = Dict(eq.species_id => eq.equation
                             for eq in $(esc(enzmldoc)).equations
                             if eq.equation_type == "ode")

            # Create time variable first
            t = eval(:(@independent_variables t))[1]

            # Create variables with explicit type
            vars = Dict{String,Symbol}()
            for v in keys(equations)
                vars[v] = Symbol(v)
            end

            # Create parameters
            params = Dict{String,Symbolics.Num}()
            for p in param_symbols
                params[p] = eval(:(@parameters $(Symbol(p))))[1]
            end

            # Create differential operator
            D = Differential(t)

            # Create equations using the symbolic variables
            ode_eqs = [
                D(eval(:(@variables $(Symbol(v))(t)))[1]) ~ eval(Meta.parse(eq))
                for (v, eq) in equations
            ]

            # Create and return the system
            sys = ODESystem(ode_eqs, t, name=:sys)
            (structural_simplify(sys), vars, params)
        end
    end
end

"""
    @prob_func(prob::ODEProblem)

Formulates a prob_func for usage in an EnsembleProblem.

# Arguments
- `prob::ODEProblem`: The ODE problem to create the function for
- `u0s`: Vector of initial conditions

# Returns
- A function that extracts the initial conditions from a vector of dictionaries
"""
macro prob_func(prob::Symbol, u0s::Symbol)
    quote
        function prob_func(prob, i, repeat)
            remake($(esc(prob)), u0=$(esc(u0s))[i])
        end
    end
end

export @system, @prob_func

end # module System