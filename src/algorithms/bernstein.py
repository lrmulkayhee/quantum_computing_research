from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def bernstein_algorithm(parameters):
    """
    Bernstein-Vazirani algorithm implementation.
    
    Args:
        parameters (dict): The parameters for Bernstein-Vazirani algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    hidden_string = parameters.get('hidden_string', '1')
    num_qubits = len(hidden_string)
    
    # Create a Quantum Circuit with num_qubits + 1 qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits + 1, num_qubits)
    
    # Apply Hadamard gates
    qc.h(range(num_qubits + 1))
    
    # Apply X gate to the last qubit
    qc.x(num_qubits)
    
    # Apply Hadamard gate to the last qubit
    qc.h(num_qubits)
    
    # Oracle for hidden string
    for i, bit in enumerate(hidden_string):
        if bit == '1':
            qc.cx(i, num_qubits)
    
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

def run_bernstein(parameters):
    """
    Run Bernstein-Vazirani algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Bernstein-Vazirani algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run Bernstein-Vazirani algorithm with the given parameters
    result_counts = bernstein_algorithm(parameters)
    
    # Calculate accuracy
    hidden_string = parameters.get('hidden_string', '1')
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get(hidden_string, 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}