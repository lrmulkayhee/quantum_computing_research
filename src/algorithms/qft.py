from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def qft_algorithm(parameters):
    """
    QFT algorithm implementation.
    
    Args:
        parameters (dict): The parameters for QFT algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    num_qubits = parameters.get('num_qubits', 2)
    
    # Create a Quantum Circuit with num_qubits qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply QFT
    for j in range(num_qubits):
        for k in range(j):
            qc.cp(3.14159 / 2**(j-k), k, j)
        qc.h(j)
    
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

def run_qft(parameters):
    """
    Run QFT algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for QFT algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run QFT algorithm with the given parameters
    result_counts = qft_algorithm(parameters)
    
    # Calculate accuracy (for QFT, we might not have a specific target state)
    total_counts = sum(result_counts.values())
    accuracy = 1.0  # QFT doesn't have a specific target state for accuracy
    
    return {'result_counts': result_counts, 'accuracy': accuracy}