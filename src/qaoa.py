import numpy as np
from scipy.linalg import expm
from src.mixer import mixer_operator
from src.cost import cost_operator


def cost_unitary(H_C, gamma):
    return expm(-1j * gamma * H_C)

def mixer_unitary(H_B, beta):
    return expm(-1j * beta * H_B)

def initial_state(n):
    return np.full(2**n, 1/np.sqrt(2**n), dtype=complex)

def qaoa_state(graph, n, gamma, beta):
    state = initial_state(n)
    H_C = cost_operator(graph, n)
    H_B = mixer_operator(n)
    U_C = cost_unitary(H_C, gamma)
    U_B = mixer_unitary(H_B, beta)
    return U_B @ (U_C @ state)