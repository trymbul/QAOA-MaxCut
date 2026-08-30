import matplotlib.pyplot as plt
import os

result_files = []

for n in [4, 6, 8, 10]:
    result_files.append(f"results/cycle{n}_results.txt")

results = {}

for filename in result_files:
    graph_name = os.path.basename(filename).replace("_results.txt", "")

    p_values = []
    expectations = []
    evaluations = []
    quantum_gates = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("p:"):
                p_values.append(int(line.split(":")[1]))

            elif line.startswith("Best expectation:"):
                expectations.append(float(line.split(":")[1]))

            elif line.startswith("Evaluations for best run:"):
                evaluations.append(int(line.split(":")[1]))
            elif line.startswith("Total quantum gates:"):
                quantum_gates.append(int(line.split(":")[1]))

    results[graph_name] = {
        "p": p_values,
        "expectations": expectations,
        "evaluations": evaluations,
        "quantum_gates": quantum_gates
    }


for graph_name, data in results.items():

    plt.plot(
        data["p"],
        data["expectations"],
        marker="o"
    )

    plt.xlabel("QAOA depth p")
    plt.ylabel("Best expectation value")
    plt.title(f"QAOA performance vs. circuit depth ({graph_name})")

    plt.savefig(
        f"figures/comparisons/{graph_name}/expectation_vs_p.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


    plt.plot(
        data["p"],
        data["evaluations"],
        marker="o"
    )

    plt.xlabel("QAOA depth p")
    plt.ylabel("Optimizer evaluations")
    plt.title(f"Optimization cost vs. QAOA depth ({graph_name})")

    plt.savefig(
        f"figures/comparisons/{graph_name}/evaluations_vs_p.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

for graph_name, data in results.items():
    plt.plot(
        data["p"],
        data["expectations"],
        marker="o",
        label=graph_name
    )

plt.xlabel("QAOA depth p")
plt.ylabel("Best expectation value")
plt.title("QAOA performance vs. circuit depth")
plt.legend()

plt.savefig(
    "figures/comparisons/expectation_vs_p_all.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

classical_results = {}

with open("results/classical_heuristic_results.txt", "r") as file:
    current_graph = None

    for line in file:
        line = line.strip()

        if line.startswith("Graph:"):
            current_graph = line.split(":")[1].strip()
            classical_results[current_graph] = {}

        elif line.startswith("Best cut:"):
            classical_results[current_graph]["best_cut"] = float(
                line.split(":")[1]
            )

        elif line.startswith("Average cut:"):
            classical_results[current_graph]["average_cut"] = float(
                line.split(":")[1]
            )
        elif line.startswith("Total operations:"):
            classical_results[current_graph]["operations"] = int(
                line.split(":")[1]
            )


optimal_results = {}

with open("results/classical_results.txt", "r") as file:
    current_graph = None

    for line in file:
        line = line.strip()

        if line.startswith("Graph:"):
            current_graph = line.split(":")[1].strip()
            optimal_results[current_graph] = {}

        elif line.startswith("Optimal cut:"):
            optimal_results[current_graph]["optimal_cut"] = float(
                line.split(":")[1]
            )
        elif line.startswith("Operations:"):
            optimal_results[current_graph]["operations"] = int(
                line.split(":")[1]
            )

graph_names = ["cycle4", "cycle6", "cycle8", "cycle10"]

for graph_name in graph_names:
    optimal = optimal_results[graph_name]["optimal_cut"]

    p_values = results[graph_name]["p"]

    qaoa_performance = [
        value / optimal
        for value in results[graph_name]["expectations"]
    ]

    classical_best = (
        classical_results[graph_name]["best_cut"] / optimal
    )

    classical_average = (
        classical_results[graph_name]["average_cut"] / optimal
    )

    plt.plot(
        p_values,
        qaoa_performance,
        marker="o",
        label="QAOA"
    )

    plt.axhline(
        classical_best,
        linestyle="--",
        label="Classical local search (best)"
    )

    plt.axhline(
        classical_average,
        linestyle="-.",
        label="Classical local search (average)"
    )

    plt.scatter(
        [p_values[-1]],
        [1.0],
        marker="x",
        s=80,
        label="Optimal"
    )

    plt.xlabel("QAOA depth p")
    plt.ylabel("Solution quality / optimal cut")
    plt.title(f"QAOA vs. classical local search ({graph_name})")
    plt.ylim(0, 1.05)
    plt.legend()

    plt.savefig(
        f"figures/comparisons/{graph_name}/qaoa_vs_classical.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # Plot computational operations

plt.figure(figsize=(10, 6))

for p in [1, 2, 3]:
    plt.plot(
        [4, 6, 8, 10],
        [
            results[f"cycle{n}"]["quantum_gates"][p - 1]
            for n in [4, 6, 8, 10]
        ],
        marker="o",
        label=f"QAOA p={p}"
    )

# p=4 exists only for n=4, 6, 8
plt.plot(
    [4, 6, 8],
    [
        results[f"cycle{n}"]["quantum_gates"][3]
        for n in [4, 6, 8]
    ],
    marker="o",
    label="QAOA p=4"
)

plt.plot(
    [4, 6, 8, 10],
    [
        optimal_results[f"cycle{n}"]["operations"]
        for n in [4, 6, 8, 10]
    ],
    marker="o",
    label="Classical brute force"   
)

plt.plot(
    [4, 6, 8, 10],
    [
        classical_results[f"cycle{n}"]["operations"]
        for n in [4, 6, 8, 10]
    ],
    marker="o",
    label="Classical local search"
)
plt.yscale("log")

plt.xlabel("Number of vertices n")
plt.ylabel("Operations")
plt.title("Computational operations: QAOA vs. classical algorithms")
plt.legend()

plt.savefig(
    "figures/comparisons/operations_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()