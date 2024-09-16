from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit import Aer, execute

def plot_results(circuit):
    """Execute the circuit and plot the results."""
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    return plot_histogram(counts)

def plot_statevector(circuit):
    """Execute the circuit and plot the statevector."""
    simulator = Aer.get_backend('statevector_simulator')
    job = execute(circuit, simulator)
    result = job.result()
    statevector = result.get_statevector(circuit)
    return plot_bloch_multivector(statevector)