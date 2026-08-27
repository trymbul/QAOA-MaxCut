import numpy as np
from src.cost import cost_operator
from src.qaoa import cost_unitary, mixer_unitary, initial_state, qaoa_state, qaoa_expectation
from src.mixer import mixer_operator
from scipy.linalg import expm


def test_cost_unitary_on_state():
    graph = [(0, 1), (1, 2), (0, 2)]

    H_C = cost_operator(graph, 3)

    state = np.array([0, 0, 1, 0, 0, 0, 0, 0],
        dtype=complex)

    gamma = 0.5

    result = cost_unitary(H_C, gamma) @ state

    expected = np.exp(-1j * 2 * gamma) * state

    assert np.allclose(result, expected)

def test_mixer_unitary():
    H_B = mixer_operator(2)
    beta = 0.5

    result = mixer_unitary(H_B, beta)

    expected = expm(-1j * beta * H_B)

    assert np.allclose(result, expected)

def test_initial_state():
    result = initial_state(3)

    expected = np.ones(8, dtype=complex) / np.sqrt(8)

    assert np.allclose(result, expected)

def test_qaoa_state_normalized():
    graph = [(0, 1), (1, 2), (0, 2)]

    state = qaoa_state(
        graph,
        3,
        gamma=0.5,
        beta=0.3
    )

    assert np.isclose(np.linalg.norm(state), 1)

def test_qaoa_state_order():
    graph = [(0, 1), (1, 2), (0, 2)]

    gamma = 0.5
    beta = 0.3

    state = initial_state(3)

    H_C = cost_operator(graph, 3)
    H_B = mixer_operator(3)

    U_C = cost_unitary(H_C, gamma)
    U_B = mixer_unitary(H_B, beta)

    expected = U_B @ (U_C @ state)

    result = qaoa_state(graph, 3, gamma, beta)

    assert np.allclose(result, expected)

def test_qaoa_expectation():
    graph = [(0, 1), (1, 2), (0, 2)]
    results = []
    gammas = [0, 0.5, 1.0]
    for gamma in gammas:
        results.append(qaoa_expectation(graph, 3, gamma, beta=0.3))

    assert len(results) == 3 and all(0 <= result <= 2 for result in results )