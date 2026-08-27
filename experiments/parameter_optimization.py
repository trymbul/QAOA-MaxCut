import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from src.measurement import index_to_bitstring
from src.qaoa import qaoa_expectation_pn, qaoa_state_pn


graph = [(0, 1), (1, 2), (2, 3), (3, 0)]
graph_name = "cycle4"
n = 4
p = 2
probability_filename = (
    f"figures/p{p}/measurement_probabilities_{graph_name}.png"
)

def objective(parameters):
    global count
    gammas = parameters[:p]
    betas = parameters[p:]
    return -qaoa_expectation_pn(graph, n, gammas, betas)


initial_parameters = np.random.uniform(0, np.pi, 2 * p)

result = minimize(objective, initial_parameters, method="COBYLA")

best_parameters = result.x
count = result.nfev

best_gammas = best_parameters[:p]
best_betas = best_parameters[p:]

best_expectation = -result.fun

states = qaoa_state_pn(graph, n, best_gammas, best_betas)
probabilities = np.abs(states)**2

plt.figure(figsize=(10, 5))
states = [index_to_bitstring(i, n) for i in range(2**n)]
plt.bar(states, probabilities)

plt.xticks(rotation=45, ha="right")

plt.xlabel("State")
plt.ylabel("Probability")
plt.title("QAOA measurement probabilities")
plt.savefig(probability_filename, dpi=300, bbox_inches="tight")
plt.close()

with open("results/qaoa_results.txt", "a") as file:
    file.write(f"Graph: {graph_name}\n")
    file.write(f"n: {n}\n")
    file.write(f"p: {p}\n")
    file.write(f"Best expectation: {best_expectation:.8f}\n")
    file.write(f"Best gammas: {best_gammas}\n")
    file.write(f"Best betas: {best_betas}\n")
    file.write(f"Optimizer evaluations: {count}\n")
    file.write("\n")