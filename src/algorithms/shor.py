from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
from math import gcd
import random
import time

def qpe_amod15(a):
    n_count = 8
    qc = QuantumCircuit(4 + n_count, n_count)
    for q in range(n_count):
        qc.h(q)  # Initialize counting qubits in state |+>
    qc.x(3 + n_count)  # And auxiliary register in state |1>
    for q in range(n_count):  # Do controlled-U operations
        qc.append(c_amod15(a, 2**q), [q] + [i + n_count for i in range(4)])
    qc.append(qft_dagger(n_count), range(n_count))  # Do inverse-QFT
    qc.measure(range(n_count), range(n_count))
    return qc

def c_amod15(a, power):
    """Controlled multiplication by a mod 15"""
    U = QuantumCircuit(4)
    for iteration in range(power):
        if a in [2, 13]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
        if a in [7, 8]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
        if a in [4, 11]:
            U.swap(1, 3)
            U.swap(0, 2)
        if a in [7, 11, 8, 13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = "%i^%i mod 15" % (a, power)
    c_U = U.control()
    return c_U

def qft_dagger(n):
    """n-qubit QFTdagger the first n qubits in circ"""
    qc = QuantumCircuit(n)
    for qubit in range(n // 2):
        qc.swap(qubit, n - qubit - 1)
    for j in range(n):
        for m in range(j):
            qc.cp(-np.pi / float(2 ** (j - m)), m, j)
        qc.h(j)
    qc.name = "QFT†"
    return qc

def shor_algorithm(N):
    """
    Run Shor's algorithm to factorize the given number N.
    
    Args:
        N (int): The number to factorize.
        
    Returns:
        tuple: The factors of N.
    """
    if N % 2 == 0:
        return 2, N // 2

    def get_order(a, N):
        qc = qpe_amod15(a)
        aer_sim = AerSimulator()
        t_qc = transpile(qc, aer_sim)
        result = aer_sim.run(t_qc).result()  # Run the transpiled circuit directly
        counts = result.get_counts()
        plot_histogram(counts)
        plt.close()  # Close the figure after plotting
        phase = max(counts, key=counts.get)
        phase = int(phase, 2) / (2 ** 8)
        if phase == 0:
            raise ValueError("Phase is zero, cannot calculate order.")
        order = int(1 / phase)
        return order

    while True:
        a = random.randint(2, N - 1)
        if gcd(a, N) != 1:
            return gcd(a, N), N // gcd(a, N)
        try:
            order = get_order(a, N)
        except ValueError:
            continue  # Retry with a different 'a' if phase is zero
        if order % 2 == 0:
            factor1 = gcd(a ** (order // 2) - 1, N)
            factor2 = gcd(a ** (order // 2) + 1, N)
            if factor1 != 1 and factor2 != 1:
                return factor1, factor2

def run_shor(parameters):
    """
    Run Shor's algorithm with the given parameters.
    
    Args:
        parameters (dict): The parameters for Shor's algorithm.
        
    Returns:
        dict: The factors of the number and accuracy.
    """
    N = parameters['number']
    start_time = time.time()
    factor1, factor2 = shor_algorithm(N)
    execution_time = time.time() - start_time
    
    # Calculate accuracy
    correct_factors = (factor1 * factor2 == N)
    accuracy = 1.0 if correct_factors else 0.0
    
    return {'factor1': factor1, 'factor2': factor2, 'accuracy': accuracy, 'execution_time': execution_time}

if __name__ == "__main__":
    # Example usage
    parameters = {'number': 15}
    print(run_shor(parameters))