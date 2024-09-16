from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def qpe_algorithm():
    # Create a Quantum Circuit with 3 qubits and 3 classical bits
    qc = QuantumCircuit(3, 3)
    
    # Apply Hadamard gates
    qc.h([0, 1])
    
    # Apply controlled-U gates
    qc.cp(1.0, 0, 2)
    qc.cp(2.0, 1, 2)
    
    # Apply inverse QFT
    qc.h([0, 1])
    
    # Measure the qubits
    qc.measure([0, 1, 2], [0, 1, 2])
    
    # Execute the circuit on the qasm simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    
    # Get the counts and plot the histogram
    counts = result.get_counts(qc)
    plot_histogram(counts)
    
    return counts

if __name__ == "__main__":
    print(qpe_algorithm())