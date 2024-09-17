from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from qiskit.extensions import UnitaryGate
import numpy as np

def create_hhl_circuit(matrix, vector, num_ancillae):
    """
    Create the HHL circuit for solving the linear system Ax = b.
    
    Args:
        matrix (np.ndarray): The matrix A.
        vector (np.ndarray): The vector b.
        num_ancillae (int): The number of ancilla qubits for QPE.
        
    Returns:
        QuantumCircuit: The HHL quantum circuit.
    """
    num_qubits = int(np.log2(matrix.shape[0]))
    total_qubits = num_qubits + num_ancillae + 1
    
    # Create a Quantum Circuit
    qc = QuantumCircuit(total_qubits, num_qubits)
    
    # Step 1: Prepare the state |b>
    for i in range(num_qubits):
        if vector[i] == 1:
            qc.x(i)
    
    # Step 2: Apply Quantum Phase Estimation (QPE)
    qpe = QuantumCircuit(total_qubits)
    qpe.h(range(num_qubits, num_qubits + num_ancillae))
    for i in range(num_ancillae):
        qc.append(UnitaryGate(matrix).control(), [num_qubits + i] + list(range(num_qubits)))
    qpe.append(QFT(num_ancillae).inverse(), range(num_qubits, num_qubits + num_ancillae))
    qc.append(qpe, range(total_qubits))
    
    # Step 3: Apply controlled rotations based on the eigenvalues
    for i in range(num_ancillae):
        angle = 2 * np.pi / (2 ** (i + 1))
        qc.cry(angle, num_qubits + num_ancillae, num_qubits + i)
    
    # Step 4: Apply inverse QPE
    qc.append(QFT(num_ancillae), range(num_qubits, num_qubits + num_ancillae))
    for i in range(num_ancillae):
        qc.append(UnitaryGate(matrix).control(), [num_qubits + i] + list(range(num_qubits)))
    qc.h(range(num_qubits, num_qubits + num_ancillae))
    
    # Step 5: Uncompute the eigenvector preparation
    for i in range(num_qubits):
        if vector[i] == 1:
            qc.x(i)
    
    # Measure the qubits
    qc.measure(range(num_qubits), range(num_qubits))
    
    return qc

def run_hhl(matrix, vector, num_ancillae):
    """
    Run the HHL algorithm with the given matrix and vector.
    
    Args:
        matrix (np.ndarray): The matrix A.
        vector (np.ndarray): The vector b.
        num_ancillae (int): The number of ancilla qubits for QPE.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Create the HHL circuit
    qc = create_hhl_circuit(matrix, vector, num_ancillae)
    
    # Execute the circuit on the AerSimulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    
    # Get the counts and plot the histogram
    counts = result.get_counts(compiled_circuit)
    plot_histogram(counts)
    
    return counts
