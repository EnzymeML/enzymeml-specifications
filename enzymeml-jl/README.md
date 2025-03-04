# EnzymeML.jl

This is the Julia implementation of the data format EnzymeML. It provides interfaces to commonly used modelling packages like DifferentialEquations.jl and ModelingToolkit.jl.

## Installation

> The EnzymeML.jl package is still under development and not yet registered. Please clone the repository and add it to your local Julia package environment.

```julia
] add EnzymeML
```

## Usage

The EnzymeML.jl package provides ready-made functions and macros to extract the ODE system, initial conditions, and parameters from an EnzymeML document. These can be used to directly create an `ODEProblem` from an EnzymeML document and perform parameter estimation and beyond.

In the following example, we load an EnzymeML document from a JSON file and extract the ODE system, initial conditions, and parameters. We then create an `ODEProblem` from the extracted data and solve it using the `EnsembleProblem` interface.

```julia
using EnzymeML
using DifferentialEquations
using Plots

json_string = read("./test.json", String)

# Parse JSON into a mutable struct
enzmldoc = JSON3.read(json_string, EnzymeMLDocument)

# Create the ODE system directly from the document
sys, vars, params = @system(enzmldoc)

# Extract the initial conditions for each measurement
u0s = extract_measurements(enzmldoc, vars)
p = extract_parameters(enzmldoc, params)

# Define the time span
tspan = (0.0, 200.0)

# Create the base ODEProblem
prob = ODEProblem(sys, first(u0s), tspan, p)

# Formulate a prob_func for usage in an EnsembleProblem
prob_func = @prob_func(prob, u0s)

# Create an EnsembleProblem
ensemble_prob = EnsembleProblem(prob, prob_func=prob_func)

# Solve the EnsembleProblem
ensemble_sol = solve(ensemble_prob, Tsit5(), EnsembleThreads(), 
```

