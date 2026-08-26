from src.cost import edge_operator, edge_cost_operator, cost_operator, expectation_value
import numpy as np
from src.gates import Z

def test_edge_operator_01():
    result = edge_operator(Z, 0, 1, 2)

    expected = np.diag([1, -1, -1, 1])

    assert np.allclose(result, expected)


def test_edge_operator_order():
    result_01 = edge_operator(Z, 0, 1, 2)
    result_10 = edge_operator(Z, 1, 0, 2)

    assert np.allclose(result_01, result_10)

def test_edge_operator_3_qubits():
    result = edge_operator(Z, 1, 2, 3)

    expected = np.diag([1, -1, -1, 1, 1, -1, -1, 1])

    assert np.allclose(result, expected)

def test_edge_cost_operator():
    result = edge_cost_operator(0, 1, 2)

    expected = np.diag([0, 1, 1, 0])

    assert np.allclose(result, expected)

def test_edge_cost_operator_3_qubits():
    result = edge_cost_operator(1, 2, 3)

    expected = np.diag([0, 1, 1, 0, 0, 1, 1, 0])

    assert np.allclose(result, expected)


def test_cost_operator_triangle():
    graph = [(0, 1), (1, 2), (0, 2)]

    result = cost_operator(graph, 3)

    expected = np.diag([0, 2, 2, 2, 2, 2, 2, 0])

    assert np.allclose(result, expected)


def test_cost_operator_on_state():
    graph = [(0, 1), (1, 2), (0, 2)]

    operator = cost_operator(graph, 3)

    state = np.array([0, 0, 1, 0, 0, 0, 0, 0], dtype=complex)

    result = operator @ state

    expected = 2 * state

    assert np.allclose(result, expected)

def test_expectation_value():
    graph = [(0, 1), (1, 2), (0, 2)]

    operator = cost_operator(graph, 3)

    state = np.array(
        [1/np.sqrt(2), 0, 1/np.sqrt(2), 0, 0, 0, 0, 0],
        dtype=complex
    )

    result = expectation_value(operator, state)

    assert np.isclose(result, 1)

def test_expectation_value():
    graph = [(0, 1), (1, 2), (0, 2)]

    operator = cost_operator(graph, 3)

    state = np.array(
        [1/np.sqrt(2), 0, 1/np.sqrt(2), 0, 0, 0, 0, 0],
        dtype=complex
    )

    result = expectation_value(operator, state)

    assert np.isclose(result, 1)