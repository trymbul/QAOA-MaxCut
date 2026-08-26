import numpy as np
from src.gates import X
from src.mixer import mixer_operator


def test_mixer_operator_3_qubits():
    result = mixer_operator(3)

    X0 = np.kron(np.kron(X, np.eye(2)), np.eye(2))
    X1 = np.kron(np.kron(np.eye(2), X), np.eye(2))
    X2 = np.kron(np.kron(np.eye(2), np.eye(2)), X)

    expected = X0 + X1 + X2

    assert np.allclose(result, expected)