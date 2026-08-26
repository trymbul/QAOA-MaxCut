from src.maxcut import cut_value, maxcut_brute
from src.measurement import index_to_bitstring

graph = [(0, 1), (0, 2), (1, 2)]

def test_cut_value():
    partitions=[[0,0,0], [0,1,1], [0,1,0], [1,0,0]]
    results = [0,2,2,2]
    for part, result in zip(partitions, results):
        assert cut_value(graph, part) == result


def test_maxcut_brute():
    best_cut, partitions = maxcut_brute(graph, 3)
    assert best_cut == 2 and len(partitions) == 6