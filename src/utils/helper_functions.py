import numpy as np
from qiskit import QuantumCircuit

def apply_hadamard_all(qubits):
    """
    Apply Hadamard gate to all qubits in the given QuantumCircuit.
    
    Parameters:
    qubits (QuantumCircuit): The quantum circuit to which the Hadamard gates will be applied.
    
    Returns:
    QuantumCircuit: The quantum circuit with Hadamard gates applied to all qubits.
    """
    for qubit in range(qubits.num_qubits):
        qubits.h(qubit)
    return qubits

def create_superposition_state(num_qubits):
    """
    Create a quantum circuit that puts all qubits into a superposition state.
    
    Parameters:
    num_qubits (int): The number of qubits in the quantum circuit.
    
    Returns:
    QuantumCircuit: The quantum circuit with all qubits in a superposition state.
    """
    qc = QuantumCircuit(num_qubits)
    qc = apply_hadamard_all(qc)
    return qc

def measure_all(qubits):
    """
    Add measurement operations to all qubits in the given QuantumCircuit.
    
    Parameters:
    qubits (QuantumCircuit): The quantum circuit to which the measurement operations will be added.
    
    Returns:
    QuantumCircuit: The quantum circuit with measurement operations added to all qubits.
    """
    for qubit in range(qubits.num_qubits):
        qubits.measure(qubit, qubit)
    return qubits

def normalize_vector(vector):
    """
    Normalize a given vector.
    
    Parameters:
    vector (np.ndarray): The vector to be normalized.
    
    Returns:
    np.ndarray: The normalized vector.
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm

def tensor_product(state1, state2):
    """
    Compute the tensor product of two quantum states.
    
    Parameters:
    state1 (np.ndarray): The first quantum state.
    state2 (np.ndarray): The second quantum state.
    
    Returns:
    np.ndarray: The tensor product of the two quantum states.
    """
    return np.kron(state1, state2)