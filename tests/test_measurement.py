from src.measurement import measure, index_to_bitstring, measure_bitstring
from src.quantum_state import state_0, state_1, state_p, state_m, state_00, state_01, state_10, state_11, is_normalized, tensor_product
from src.gates import X, Z, H, I, apply_gate, single_qubit_operator
import numpy as np

def test_measure_deterministic_zero():
    for _ in range(100):
        assert measure(state_0) == 0


def test_measure_deterministic_one():
    for _ in range(100):
        assert measure(state_1) == 1


def test_measure_plus():
    results = [measure(state_p) for _ in range(1000)]

    fraction_zero = results.count(0) / 1000
    fraction_one = results.count(1) / 1000

    assert 0.4 < fraction_zero < 0.6
    assert 0.4 < fraction_one < 0.6

def test_measure_two_qubit_state():
    state = np.array([0, 0, 1, 0], dtype=complex)

    for _ in range(100):
        assert measure(state) == 2


def test_measure_three_qubit_state():
    state = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=complex)

    for _ in range(100):
        assert measure(state) == 7

def test_index_to_bitstring():
    assert index_to_bitstring(0, 3) == "000"
    assert index_to_bitstring(1, 3) == "001"
    assert index_to_bitstring(2, 3) == "010"
    assert index_to_bitstring(3, 3) == "011"
    assert index_to_bitstring(4, 3) == "100"
    assert index_to_bitstring(5, 3) == "101"
    assert index_to_bitstring(6, 3) == "110"
    assert index_to_bitstring(7, 3) == "111"

def test_measure_bitstring_zero():
    assert measure_bitstring(state_0) == "0"


def test_measure_bitstring_one():
    assert measure_bitstring(state_1) == "1"


def test_measure_bitstring_two_qubits():
    state = np.array([0, 0, 1, 0], dtype=complex)

    for _ in range(100):
        assert measure_bitstring(state) == "10"


def test_measure_bitstring_three_qubits():
    state = np.array([0, 0, 0, 0, 0, 0, 0, 1], dtype=complex)

    for _ in range(100):
        assert measure_bitstring(state) == "111"