from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def deutsch_algorithm(parameters):
    """
    Deutsch-Jozsa algorithm implementation.
    
    Args:
        parameters (dict): The parameters for Deutsch-Jozsa algorithm.
        
    Returns:
        dict: The result counts from the execution.
    """
    oracle_type = parameters.get('oracle_type', 'constant')
    num_qubits = parameters.get('num_qubits', 1)
    
    # Create a Quantum Circuit with num_qubits + 1 qubits and num_qubits classical bits
    qc = QuantumCircuit(num_qubits + 1, num_qubits)
    
    # Apply Hadamard gates
    qc.h(range(num_qubits + 1))
    
    # Apply X gate to the last qubit
    qc.x(num_qubits)
    
    # Apply Hadamard gate to the last qubit
    qc.h(num_qubits)
    
    # Oracle for constant or balanced function
    if oracle_type == 'constant':
        pass  # Do nothing for constant function
    elif oracle_type == 'balanced':
        qc.cx(0, num_qubits)
    
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

def run_deutsch(parameters):
    """
    Run Deutsch-Jozsa algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Deutsch-Jozsa algorithm.
        
    Returns:
        dict: The result counts and accuracy from the execution.
    """
    
    # Run Deutsch-Jozsa algorithm with the given parameters
    result_counts = deutsch_algorithm(parameters)
    
    # Calculate accuracy
    oracle_type = parameters.get('oracle_type', 'constant')
    total_counts = sum(result_counts.values())
    correct_counts = result_counts.get('0' * parameters.get('num_qubits', 1), 0)
    accuracy = correct_counts / total_counts if total_counts > 0 else 0
    
    return {'result_counts': result_counts, 'accuracy': accuracy}