from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def quantum_key_distribution_algorithm(parameters):
    """
    Quantum Key Distribution algorithm implementation.
    
    Args:
        parameters (dict): The parameters for Quantum Key Distribution algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    num_qubits = parameters.get('num_qubits', 3)
    
    # Create a Quantum Circuit with num_qubits qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Quantum Key Distribution steps (simplified example)
    qc.h(range(num_qubits))
    qc.cx(0, 1)
    qc.h(range(num_qubits))
    
    # Measure the qubits
    qc.measure(range(num_qubits), range(num_qubits))
    
    # Execute the circuit on the AerSimulator
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    
    # Get the counts and plot the histogram
    counts = result.get_counts(compiled_circuit)
    plot_histogram(counts)
    
    return counts

def run_quantum_key_distribution(parameters):
    """
    Run Quantum Key Distribution algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Quantum Key Distribution algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run Quantum Key Distribution algorithm with the given parameters
    result_counts = quantum_key_distribution_algorithm(parameters)
    
    # Calculate accuracy (example calculation, adjust as needed)
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get('0' * parameters.get('num_qubits', 3), 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}