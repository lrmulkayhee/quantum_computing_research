from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def grover_algorithm(parameters):
    """
    Grover's algorithm implementation.
    
    Args:
        parameters (dict): The parameters for Grover's algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    target_state = parameters.get('target_state', '11')
    num_qubits = parameters.get('num_qubits', 2)
    
    # Create a Quantum Circuit with num_qubits qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply Hadamard gates
    qc.h(range(num_qubits))
    
    # Oracle for target_state (example for |11>)
    if target_state == '11':
        qc.cz(0, 1)
    
    # Apply Hadamard gates again
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

def run_grover(parameters):
    """
    Run Grover's algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Grover's algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run Grover's algorithm with the given parameters
    result_counts = grover_algorithm(parameters)
    
    # Calculate accuracy
    target_state = parameters.get('target_state', '11')
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get(target_state, 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}