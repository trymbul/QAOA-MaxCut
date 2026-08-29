from src.classical_heuristic import local_search_maxcut
from src.graphs import cycle_graph
from src.measurement import partition_to_bitstring

n_values = [4, 6, 8]
num_runs = 10

with open("results/classical_heuristic_results.txt", "w") as file:
    for n in n_values:
        graph = cycle_graph(n)

        best_cut = 0
        total_cut = 0

        for i in range(num_runs):
            cut, partition = local_search_maxcut(graph, n)

            total_cut += cut

            if cut > best_cut:
                best_cut = cut
                best_partition = partition

        average_cut = total_cut / num_runs

        file.write(f"Graph: cycle{n}\n")
        file.write(f"n: {n}\n")
        file.write(f"Best cut: {best_cut}\n")
        file.write(f"Average cut: {average_cut:.4f}\n")
        file.write(f"Best partition: {partition_to_bitstring(best_partition)}\n")
        file.write(f"Number of runs: {num_runs}\n")
        file.write("\n")