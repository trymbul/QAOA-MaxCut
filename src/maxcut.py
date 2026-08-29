from src.measurement import index_to_bitstring

def cut_value(graph, partition):
    cut = 0
    for kant in graph:
        if partition[kant[0]] != partition[kant[1]]:
            cut += 1

    return cut

def maxcut_brute(graph, n):
    best_cut = 0
    best_partitions = []
    operations = 0
    for i in range(2**n):
        partition = [int(j) for j in index_to_bitstring(i, n)]
        cut = cut_value(graph, partition)
        operations += 1
        if cut > best_cut:
            best_cut = cut
            best_partitions = [partition]
        elif cut == best_cut:
            best_partitions.append(partition)
    return best_cut, best_partitions, operations