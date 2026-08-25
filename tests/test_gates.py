import numpy as np
from src.quantum_state import state_0, state_1, state_p, state_m, state_00, state_01, state_10, state_11, is_normalized, tensor_product
from src.gates import X, Z, H, I, apply_gate, single_qubit_operator

def test_Xon0():
    result = apply_gate(X, state_0)
    assert np.allclose(result, state_1)

def test_Hon0():
    result = apply_gate(H, state_0)
    assert np.allclose(result, state_p)

def test_Hon1():
    result = apply_gate(H, state_1)
    assert np.allclose(result, state_m)

def test_ZonP():
    result = apply_gate(Z, state_p)
    assert np.allclose(result, state_m)

def test_Zon0():
    result = apply_gate(Z, state_0)
    assert np.allclose(result, state_0)

def test_tensor_product_00():
    result = tensor_product(state_0, state_0)
    assert np.allclose(state_00, result)

def test_tensor_product_01():
    result = tensor_product(state_0, state_1)
    assert np.allclose(state_01, result)

def test_tensor_product_10():
    result = tensor_product(state_1, state_0)
    assert np.allclose(state_10, result)

def test_tensor_product_11():
    result = tensor_product(state_1, state_1)
    assert np.allclose(state_11, result)

def test_tensor_product_plus_plus():
    result = tensor_product(state_p, state_p)
    assert np.allclose(np.array([1,1,1,1], dtype=complex)/2, result)

def test_H_on_first_qubit():
    state_00 = tensor_product(state_0, state_0)
    HxI = tensor_product(H, I)

    result = apply_gate(HxI, state_00)

    expected = np.array([1, 0, 1, 0], dtype=complex) / np.sqrt(2)

    assert np.allclose(result, expected)

def test_H_on_second_qubit():
    state_00 = tensor_product(state_0, state_0)
    IxH = tensor_product(I, H)

    result = apply_gate(IxH, state_00)

    expected = np.array([1, 1, 0, 0], dtype=complex) / np.sqrt(2)

    assert np.allclose(result, expected)

def test_single_qubit_operator_first():
    operator = single_qubit_operator(H, 0, 3)

    expected = np.kron(np.kron(H, I), I)

    assert np.allclose(operator, expected)


def test_single_qubit_operator_second():
    operator = single_qubit_operator(H, 1, 3)

    expected = np.kron(np.kron(I, H), I)

    assert np.allclose(operator, expected)


def test_single_qubit_operator_third():
    operator = single_qubit_operator(H, 2, 3)

    expected = np.kron(np.kron(I, I), H)

    assert np.allclose(operator, expected)