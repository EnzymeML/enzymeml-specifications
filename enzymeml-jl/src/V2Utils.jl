module V2Utils

using ..EnzymemlV2: EnzymeMLDocument
using Symbolics

"""
    get_initial_values(enzmldoc::EnzymeMLDocument, m_id::String, vars::Dict{String,Symbol})

Get the initial values for a given measurement ID.

# Arguments
- `enzmldoc::EnzymeMLDocument`: The EnzymeML document to get the initial values from.
- `m_id::String`: The ID of the measurement to get the initial values from.
- `vars::Dict{String,Symbol}`: A dictionary of variable names and their corresponding symbols.

# Returns
- A dictionary of variable names and their corresponding initial values.
"""
function extract_measurement(enzmldoc::EnzymeMLDocument, id::String, vars::Dict{String,Symbol})
    initial_values = Dict{Symbol,Float64}()
    for measurement in enzmldoc.measurements
        if measurement.id == id
            for species in measurement.species_data
                if species.initial !== nothing
                    initial_values[vars[species.species_id]] = species.initial
                end
            end
        end
    end
    return initial_values
end

export extract_measurement


"""
    extract_measurements(enzmldoc::EnzymeMLDocument, symbols::Dict{String,Symbol})

Extract all measurements from the EnzymeML document.

# Arguments
- `enzmldoc::EnzymeMLDocument`: The EnzymeML document to extract measurements from.
- `symbols::Dict{String,Symbol}`: A dictionary of variable names and their corresponding symbols.

# Returns
- A vector of dictionaries, each containing the initial values for a given measurement.
"""
function extract_measurements(enzmldoc::EnzymeMLDocument, symbols::Dict{String,Symbol})
    measurements = Vector{Dict{Symbol,Float64}}()
    for measurement in enzmldoc.measurements
        push!(measurements, extract_measurement(enzmldoc, measurement.id, symbols))
    end
    return measurements
end

"""
    extract_parameters(enzmldoc::EnzymeMLDocument, symbols::Dict{String,Symbol}, initials::Bool=false)

Extract all parameters from the EnzymeML document.

# Arguments
- `enzmldoc::EnzymeMLDocument`: The EnzymeML document to extract parameters from.
- `symbols::Dict{String,Symbol}`: A dictionary of parameter names and their corresponding symbols.
- `initials::Bool=false`: Whether to extract the initial values or the values.

# Returns
- A dictionary of parameter names and their corresponding parameters.
"""
function extract_parameters(enzmldoc::EnzymeMLDocument, symbols::Dict{String,Symbolics.Num}, initials::Bool=false)
    parameters = Dict{Symbolics.Num,Float64}()
    for parameter in enzmldoc.parameters
        if initials
            if parameter.initial !== nothing
                parameters[symbols[parameter.id]] = parameter.initial
            end
        else
            if parameter.value !== nothing
                parameters[symbols[parameter.id]] = parameter.value
            end
        end
    end
    return parameters
end

export extract_measurements, extract_measurement, extract_parameters

end # module V2Utils

