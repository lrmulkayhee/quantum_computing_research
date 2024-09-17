from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def qpe_algorithm(parameters):
    """
    Quantum Phase Estimation (QPE) algorithm implementation.
    
    Args:
        parameters (dict): The parameters for QPE.
        
    Returns:
        dict: The result counts from the execution.
    """
    num_qubits = parameters.get('num_qubits', 3)
    target_phase = parameters.get('target_phase', 0.25)
    
    # Create a Quantum Circuit with num_qubits qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Example QPE implementation (simplified)
    qc.h(range(num_qubits))
    qc.p(target_phase * 2 * 3.14159, range(num_qubits))
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

def run_qpe(parameters):
    """
    Run Quantum Phase Estimation (QPE) with the given parameters.
    
    Args:
        parameters (dict): The parameters for QPE.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run QPE with the given parameters
    result_counts = qpe_algorithm(parameters)
    
    # Calculate accuracy
    target_phase = parameters.get('target_phase', 0.25)
    target_state = format(int(target_phase * (2 ** parameters.get('num_qubits', 3))), 'b').zfill(parameters.get('num_qubits', 3))
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get(target_state, 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}