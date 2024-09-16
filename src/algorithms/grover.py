from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def grover_algorithm():
    # Create a Quantum Circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Apply Hadamard gates
    qc.h([0, 1])
    
    # Oracle for |11>
    qc.cz(0, 1)
    
    # Apply Hadamard gates again
    qc.h([0, 1])
    
    # Measure the qubits
    qc.measure([0, 1], [0, 1])
    
    # Execute the circuit on the qasm simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    
    # Get the counts and plot the histogram
    counts = result.get_counts(qc)
    plot_histogram(counts)
    
    return counts

if __name__ == "__main__":
    print(grover_algorithm())