import numpy as np
from src.qaoa import qaoa_expectation, qaoa_state
import matplotlib.pyplot as plt
from src.measurement import index_to_bitstring
from src.graphs import cycle_graph

n = 4
graph_name = f"cycle{n}"
graph = cycle_graph(n)

num_points_list = [50, 100, 200]
with open(f"results/{graph_name}_scan_results.txt", "w") as file:
    for num_points in (num_points_list):
        parameter_filename = (
            f"figures/p1/parameter_landscape_{graph_name}_points{num_points}.png"
        )

        probability_filename = (
            f"figures/p1/measurement_probabilities_{graph_name}_points{num_points}.png"
        )

        gammas = np.linspace(0, np.pi, num_points)
        betas = np.linspace(0, np.pi, num_points)

        values = np.zeros((num_points, num_points))

        for i in range(len(gammas)):
            for j in range(len(betas)):
                values[i, j] = qaoa_expectation(graph, n, gammas[i], betas[j])

        i, j = np.unravel_index(np.argmax(values), values.shape)

        best_value = values[i, j]
        best_gamma = gammas[i]
        best_beta = betas[j]

   
        file.write(f"Graph: {graph_name}\n")
        file.write(f"n: {n}\n")
        file.write(f"p: {1}\n")
        file.write(f"Best expectation: {best_value:.8f}\n")
        file.write(f"Best gamma: {best_gamma:.8f}\n")
        file.write(f"Best beta: {best_beta:.8f}\n")
        file.write(f"Grid points: {num_points}\n")
        file.write("\n")

        norm = plt.Normalize(vmin=0, vmax=best_value)
        img = plt.imshow(
            values,
            extent=[gammas[0], gammas[-1], betas[0], betas[-1]],
            origin="lower",
            aspect="auto",
            norm=norm
        )
        plt.scatter(best_gamma, best_beta, marker="x")
        plt.xlabel("γ")
        plt.ylabel("β")
        plt.colorbar(img, label="Expectation value")
        plt.savefig(parameter_filename, dpi=300, bbox_inches="tight")
        plt.close()

        plt.figure(figsize=(10, 5))
        state = qaoa_state(graph, n, best_gamma, best_beta)
        probabilities = np.abs(state)**2
        states = [index_to_bitstring(i, n) for i in range(2**n)]
        plt.bar(states, probabilities)

        plt.xticks(rotation=45, ha="right")

        plt.xlabel("State")
        plt.ylabel("Probability")
        plt.title("QAOA measurement probabilities")
        plt.savefig(probability_filename, dpi=300, bbox_inches="tight")
        plt.close()