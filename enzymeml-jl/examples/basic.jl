using Pkg
Pkg.develop(path=joinpath(@__DIR__, ".."))

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
ensemble_sol = solve(ensemble_prob, Tsit5(), EnsembleThreads(), trajectories=length(u0s))

# Plot the results
p1 = plot(ensemble_sol[1], idxs=[vars["substrate"], vars["product"]],
    title="Condition 1", xlabel="Time [mins]", ylabel="Concentration [mmol/l]")
p2 = plot(ensemble_sol[2], idxs=[vars["substrate"], vars["product"]],
    title="Condition 2", xlabel="Time [mins]", ylabel="Concentration [mmol/l]")

plot(p1, p2, layout=(1, 2))

# Save the plot
savefig("basic.png")