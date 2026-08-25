import numpy as np



def measure(state):
    p = np.zeros_like(state, dtype=float)
    options = np.zeros_like(state, dtype=int)
    for i in range(len(state)):
        options[i] = i
        p[i] = np.abs(state[i])**2

    return np.random.choice(options, p=p)

def index_to_bitstring(index, n_qubits):
    end = bin(index)[2:]
    start = (n_qubits-len(end))*'0'
    return start+end

def measure_bitstring(state):
    n_qubits = int(np.log2(len(state)))
    index = measure(state)
    return index_to_bitstring(index, n_qubits)