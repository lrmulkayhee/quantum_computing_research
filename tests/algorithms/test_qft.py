import unittest
from src.algorithms.qft import qft_algorithm

class TestQFT(unittest.TestCase):

    def test_qft_algorithm(self):
        # Example input for QFT
        input_state = [1, 0, 0, 0]  # Example input state (|00>)
        result = qft_algorithm(input_state)
        
        # Assertions to verify the result
        self.assertIsNotNone(result, "QFT algorithm result is None")
        self.assertTrue(isinstance(result, list), "QFT algorithm result is not a list")
        self.assertEqual(len(result), len(input_state), "QFT algorithm result length mismatch")

if __name__ == "__main__":
    unittest.main()