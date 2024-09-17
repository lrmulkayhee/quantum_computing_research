from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def simon_algorithm(parameters):
    """
    Simon's algorithm implementation.
    
    Args:
        parameters (dict): The parameters for Simon's algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    hidden_string = parameters.get('hidden_string', '11')
    num_qubits = len(hidden_string)
    
    # Create a Quantum Circuit with 2*num_qubits qubits and num_qubits classical bits
    qc = QuantumCircuit(2 * num_qubits, num_qubits)
    
    # Apply Hadamard gates to the first num_qubits
    qc.h(range(num_qubits))
    
    # Oracle for hidden string
    for i, bit in enumerate(hidden_string):
        if bit == '1':
            qc.cx(i, num_qubits + i)
    
    # Apply Hadamard gates again to the first num_qubits
    qc.h(range(num_qubits))
    
    # Measure the first num_qubits
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

def run_simon(parameters):
    """
    Run Simon's algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Simon's algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run Simon's algorithm with the given parameters
    result_counts = simon_algorithm(parameters)
    
    # Calculate accuracy
    hidden_string = parameters.get('hidden_string', '11')
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get(hidden_string, 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}