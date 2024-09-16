import unittest
from src.algorithms.shor import shor_algorithm

class TestShor(unittest.TestCase):

    def test_shor_algorithm(self):
        N = 15  # Example number to factorize
        result = shor_algorithm(N)
        self.assertIsNotNone(result, "Shor's algorithm result is None")
        self.assertTrue(isinstance(result, tuple), "Shor's algorithm result is not a tuple")
        self.assertEqual(len(result), 2, "Shor's algorithm result does not contain two factors")

if __name__ == "__main__":
    unittest.main()