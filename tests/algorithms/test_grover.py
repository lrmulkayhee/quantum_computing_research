import unittest
from qiskit import QuantumCircuit
from src.algorithms.grover import grover_search, run_grover

class TestGrover(unittest.TestCase):

    def test_grover_search(self):
        n = 3
        oracle = QuantumCircuit(n)
        oracle.cz(0, 2)
        oracle.cz(1, 2)
        
        qc = grover_search(n, oracle)
        self.assertIsNotNone(qc, "Grover's search circuit is None")
        self.assertEqual(qc.num_qubits, n, "Number of qubits mismatch")
    
    def test_run_grover(self):
        n = 3
        oracle = QuantumCircuit(n)
        oracle.cz(0, 2)
        oracle.cz(1, 2)
        
        run_grover(n, oracle)

if __name__ == "__main__":
    unittest.main()