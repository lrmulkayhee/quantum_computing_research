import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister

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
    Create a superposition state with the given number of qubits.
    
    Args:
        num_qubits (int): The number of qubits.
        
    Returns:
        QuantumCircuit: The quantum circuit with the superposition state.
    """
    qc = QuantumCircuit(num_qubits)
    for qubit in range(num_qubits):
        qc.h(qubit)
    return qc

def measure_all(qc):
    """
    Measure all qubits in the given quantum circuit.
    
    Args:
        qc (QuantumCircuit): The quantum circuit to measure.
        
    Returns:
        QuantumCircuit: The quantum circuit with measurement operations added.
    """
    num_qubits = qc.num_qubits
    qc.add_register(ClassicalRegister(num_qubits))  # Add classical bits for measurement
    qc.measure(range(num_qubits), range(num_qubits))
    return qc

def normalize_vector(vector):
    """Normalize a vector of numerical values."""
    norm = np.linalg.norm(vector)
    return vector / norm if norm != 0 else vector

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