"""
Classical Max-Cut local-search heuristic.

Based on:
"State-flipping algorithm for max cut"
https://gist.github.com/3694491

The implementation has been adapted to the graph representation
used in this project.
"""

import random
from src.maxcut import cut_value

def local_search_maxcut(graph, n):
    partition = [random.randint(0, 1) for _ in range(n)]

    improved = True

    while improved:
        improved = False

        for node in range(n):
            current_cut = cut_value(graph, partition)

            partition[node] = 1 - partition[node]

            new_cut = cut_value(graph, partition)

            if new_cut > current_cut:
                improved = True
            else:
                partition[node] = 1 - partition[node]

    return cut_value(graph, partition), partition