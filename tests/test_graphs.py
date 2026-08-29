from src.graphs import cycle_graph

def test_cycle_graph():
    assert cycle_graph(4) == [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0)
    ]