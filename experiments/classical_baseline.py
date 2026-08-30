from src.maxcut import maxcut_brute
from src.graphs import cycle_graph
from src.measurement import partition_to_bitstring

n_values = [4, 6, 8, 10]

with open("results/classical_results.txt", "w") as file:
    for n in n_values:
        graph = cycle_graph(n)

        best_cut, best_partitions, operations = maxcut_brute(graph, n)

        file.write(f"Graph: cycle{n}\n")
        file.write(f"n: {n}\n")
        file.write(f"Optimal cut: {best_cut}\n")
        file.write(f"Number of optimal partitions: {len(best_partitions)}\n")
        optimal_partitions = ", ".join(
        partition_to_bitstring(p) for p in best_partitions
        )

        file.write(f"Optimal partitions: {optimal_partitions}\n")
        file.write(f"Operations: {operations}\n") 
        file.write("\n")