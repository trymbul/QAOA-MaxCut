import numpy as np
from src.quantum_state import tensor_product

X = np.array([[0, 1], [1,0]], dtype=complex)
Z = np.array([[1, 0], [0,-1]], dtype=complex)
H = np.array([[1, 1], [1,-1]], dtype=complex)/np.sqrt(2)
I = np.array([[1, 0], [0, 1]], dtype=complex)

def apply_gate(gate, state):
    return np.matmul(gate, state)

def single_qubit_operator(gate, qubit, n_qubits):
    matrix = 1
    for i in range(n_qubits):
        operator = I
        if i == qubit:
            operator = gate
        matrix = tensor_product(matrix, operator)
    return matrix