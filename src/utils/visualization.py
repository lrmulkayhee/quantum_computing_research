from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def plot_results(circuit, filename="histogram.png"):
    """Execute the circuit and plot the results."""
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1000).result()
    counts = result.get_counts(circuit)
    histogram = plot_histogram(counts)
    histogram.savefig(filename)
    plt.show()
    return histogram

def plot_statevector(circuit, filename="statevector.png"):
    """Execute the circuit and plot the statevector."""
    simulator = AerSimulator()
    result = simulator.run(circuit).result()
    statevector = result.get_statevector(circuit)
    bloch_multivector = plot_bloch_multivector(statevector)
    bloch_multivector.savefig(filename)
    plt.show()
    return bloch_multivector