

def cycle_graph(n):
    graph = []
    for i in range(n):
        graph.append((i,(i+1)%n))
    return graph