import numpy as np
from src.gates import single_qubit_operator
from src.gates import X

def mixer_operator(n):
    operator = single_qubit_operator(X,0,n)
    for i in range(1,n):
        operator += single_qubit_operator(X, i, n)
    return operator
