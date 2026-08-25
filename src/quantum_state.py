import numpy as np

state_0 = np.array([1, 0], dtype=complex)
state_1 = np.array([0, 1], dtype=complex)
state_00 = np.array([1,0,0,0], dtype=complex)
state_01 = np.array([0,1,0,0], dtype=complex)
state_10 = np.array([0,0,1,0], dtype=complex)
state_11= np.array([0,0,0,1], dtype=complex)
state_p = np.array([1, 1], dtype=complex)/np.sqrt(2)
state_m = np.array([1, -1], dtype=complex)/np.sqrt(2)

def is_normalized(state):
    tol = 1e-4
    norm = 0
    for i in state:
        norm += np.abs(i)**2
    if 1-tol <= norm <= 1+tol:
        return True
    else : return False


def tensor_product(state1, state2):
    return np.kron(state1, state2)
