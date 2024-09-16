import unittest
from qiskit import QuantumCircuit
from src.algorithms.qpe import qpe_algorithm

class TestQPE(unittest.TestCase):

    def test_qpe_algorithm(self):
        n = 3
        qc = QuantumCircuit(n)
        qc.h(range(n))
        
        result = qpe_algorithm(qc)
        self.assertIsNotNone(result, "QPE algorithm result is None")
        self.assertTrue(isinstance(result, QuantumCircuit), "QPE algorithm result is not a QuantumCircuit")

if __name__ == "__main__":
    unittest.main()