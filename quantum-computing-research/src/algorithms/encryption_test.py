import unittest
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from encryption import encrypt, decrypt  # Assuming you have encryption and decryption functions in encryption.py

class TestQuantumEncryption(unittest.TestCase):

    def setUp(self):
        # Set up any necessary data or state before each test
        self.message = "1011"  # Example binary message
        self.key = "1101"  # Example binary key

    def test_encryption(self):
        # Test the encryption process
        encrypted_message = encrypt(self.message, self.key)
        self.assertIsNotNone(encrypted_message, "Encryption failed, result is None")
        self.assertEqual(len(encrypted_message), len(self.message), "Encrypted message length mismatch")

    def test_decryption(self):
        # Test the decryption process
        encrypted_message = encrypt(self.message, self.key)
        decrypted_message = decrypt(encrypted_message, self.key)
        self.assertEqual(decrypted_message, self.message, "Decryption failed, original message not recovered")

    def test_encryption_decryption_cycle(self):
        # Test the full encryption-decryption cycle
        encrypted_message = encrypt(self.message, self.key)
        decrypted_message = decrypt(encrypted_message, self.key)
        self.assertEqual(decrypted_message, self.message, "Encryption-Decryption cycle failed")

    def test_invalid_key(self):
        # Test decryption with an invalid key
        encrypted_message = encrypt(self.message, self.key)
        invalid_key = "0000"
        decrypted_message = decrypt(encrypted_message, invalid_key)
        self.assertNotEqual(decrypted_message, self.message, "Decryption with invalid key should not match original message")

if __name__ == "__main__":
    unittest.main()