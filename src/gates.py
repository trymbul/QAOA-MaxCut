import numpy as np

X = np.array([[0, 1], [1,0]], dtype=complex)
Z = np.array([[1, 0], [0,-1]], dtype=complex)
H = np.array([[1, 1], [1,-1]], dtype=complex)/np.sqrt(2)
I = np.array([[1, 0], [0, 1]], dtype=complex)

def apply_gate(gate, state):
    return np.matmul(gate, state)

