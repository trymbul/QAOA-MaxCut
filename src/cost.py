from src.gates import single_qubit_operator
import numpy as np
from src.gates import Z

def edge_operator(gate, qubit1, qubit2, n):
    Zi = single_qubit_operator(gate, qubit1, n)
    Zj = single_qubit_operator(gate, qubit2, n)
    return np.matmul(Zi, Zj)

def edge_cost_operator(qubit1, qubit2, n):
    I = np.eye(2**n)
    return (I - edge_operator(Z, qubit1, qubit2, n))/2

def cost_operator(graph, n):
    operator = np.zeros((2**n, 2**n), dtype=complex)
    for edge in graph:
        operator += edge_cost_operator(edge[0], edge[1], n)
    return operator

def expectation_value(operator, state):
    return np.vdot(state, operator @ state)