from qiskit import QuantumCircuit, Aer, execute
from qiskit.aqua.algorithms import Shor

def shor_algorithm(N):
    # Create a Quantum Circuit for Shor's algorithm
    shor = Shor(N)
    
    # Execute the algorithm
    result = shor.run(Aer.get_backend('qasm_simulator'))
    
    return result

if __name__ == "__main__":
    N = 15  # Example number to factorize
    print(shor_algorithm(N))