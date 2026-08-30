import numpy as np
from scipy.optimize import minimize, Bounds
import matplotlib.pyplot as plt
from src.measurement import index_to_bitstring
from src.qaoa import qaoa_expectation_pn, qaoa_state_pn, qaoa_gate_count
from src.graphs import cycle_graph

n = 4
p_list = [1, 2, 3]
graph_name = f"cycle{n}"
graph = cycle_graph(n)
def optimize_qaoa(graph, n, p):
    initial_parameters = np.random.uniform(0, np.pi, 2 * p)
    bounds = Bounds(
    np.zeros(2 * p),
    np.full(2 * p, np.pi)
)

    def objective(parameters):
        gammas = parameters[:p]
        betas = parameters[p:]
        return -qaoa_expectation_pn(graph, n, gammas, betas)
    
    result = minimize(objective, initial_parameters, method="COBYLA", bounds=bounds)
    return result

with open(f"results/{graph_name}_results.txt", "w") as file:
    for p in p_list:
        probability_filename = (
            f"figures/p{p}/measurement_probabilities_{graph_name}.png"
        )

        best_expectation = 0
        best_result = None
        total_evaluations = 0

        for i in range(10):
            result = optimize_qaoa(graph, n, p)
            expectation = -result.fun
            total_evaluations += result.nfev

            if expectation > best_expectation:
                best_expectation = expectation
                best_result = result

        best_parameters = best_result.x
        best_evaluations = best_result.nfev
        gates_per_evaluation = qaoa_gate_count(graph, n, p)
        total_quantum_gates = total_evaluations * gates_per_evaluation

        best_gammas = best_parameters[:p]
        best_betas = best_parameters[p:]


        states = qaoa_state_pn(graph, n, best_gammas, best_betas)
        probabilities = np.abs(states)**2
        if n <= 4:          # 16 states
            fontsize = 10
        elif n <= 5:        # 32 states
            fontsize = 8
        elif n <= 6:        # 64 states
            fontsize = 6
        else:               # 128+ states
            fontsize = 4

        plt.figure(figsize=(10, 5))
        states = [index_to_bitstring(i, n) for i in range(2**n)]
        plt.bar(states, probabilities)
        if n > 5:
            num_states = len(states)
            step = num_states // 32  # vis ca 32 labels
            plt.xticks(
                range(0, num_states, step),
                [states[i] for i in range(0, num_states, step)],
                rotation=45, ha="right", fontsize=fontsize
            )
        else:
            plt.xticks(rotation=45, ha="right", fontsize=fontsize)


        plt.xlabel("State")
        plt.ylabel("Probability")
        plt.title("QAOA measurement probabilities")
        plt.savefig(probability_filename, dpi=300, bbox_inches="tight")
        plt.close()

    
        file.write(f"Graph: {graph_name}\n")
        file.write(f"n: {n}\n")
        file.write(f"p: {p}\n")
        file.write(f"Best expectation: {best_expectation:.8f}\n")
        file.write(f"Best gammas: {best_gammas}\n")
        file.write(f"Best betas: {best_betas}\n")
        file.write(f"Evaluations for best run: {best_evaluations}\n")
        file.write(f"Total evaluations: {total_evaluations}\n")
        file.write(f"Quantum gates per evaluation: {gates_per_evaluation}\n")
        file.write(f"Total quantum gates: {total_quantum_gates}\n")
        file.write("\n")
        file.flush()