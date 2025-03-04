module EnzymeML

# Include the submodules in correct dependency order
include("V2.jl")
include("System.jl")
include("V2Utils.jl")

# Re-export commonly used third-party packages
using DifferentialEquations
using Symbolics
using ModelingToolkit
using Plots
using JSON3

using .EnzymemlV2
using .EnzymeMLSystem
using .V2Utils

# Export third-party packages
export DifferentialEquations, Symbolics, ModelingToolkit, Plots, JSON3

# Export our submodules and functions
export enzymeml_v2
export @system, @prob_func, @system
export extract_measurements, extract_measurement, extract_parameters

# Export the EnzymeMLDocument type
export EnzymeMLDocument

end # module EnzymeML