import unittest
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from src.algorithms.encryption import encrypt, decrypt  # Import from the new module
from src.utils.visualization import plot_results, plot_statevector  # Import visualization functions

class TestQuantumEncryption(unittest.TestCase):

    def setUp(self):
        # Set up any necessary data or state before each test
        self.message = "1011"  # Example binary message
        self.key = "1101"  # Example binary key
        self.simulator = AerSimulator()

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

    def test_empty_message(self):
        # Test encryption and decryption with an empty message
        empty_message = ""
        encrypted_message = encrypt(empty_message, self.key)
        decrypted_message = decrypt(encrypted_message, self.key)
        self.assertEqual(decrypted_message, empty_message, "Decryption of empty message failed")

    def test_different_lengths(self):
        # Test encryption and decryption with different lengths of message and key
        short_key = "1"
        encrypted_message = encrypt(self.message, short_key)
        decrypted_message = decrypt(encrypted_message, short_key)
        self.assertNotEqual(decrypted_message, self.message, "Decryption with short key should not match original message")

    def test_all_zeros(self):
        # Test encryption and decryption with all zeros
        message = "0000"
        key = "0000"
        encrypted_message = encrypt(message, key)
        decrypted_message = decrypt(encrypted_message, key)
        self.assertEqual(decrypted_message, message, "Decryption of all zeros failed")

    def test_all_ones(self):
        # Test encryption and decryption with all ones
        message = "1111"
        key = "1111"
        encrypted_message = encrypt(message, key)
        decrypted_message = decrypt(encrypted_message, key)
        self.assertEqual(decrypted_message, message, "Decryption of all ones failed")

    def test_quantum_circuit(self):
        # Create a simple quantum circuit
        qc = QuantumCircuit(1, 1)
        qc.h(0)  # Apply Hadamard gate
        qc.measure(0, 0)  # Measure qubit 0 into classical bit 0

        # Visualize the quantum circuit results
        plot_results(qc, filename="simple_circuit_histogram.png")

        # Execute the circuit on the AerSimulator
        result = self.simulator.run(qc).result()
        counts = result.get_counts(qc)

        # Check that the result is as expected (approximately equal superposition)
        self.assertIn('0', counts)
        self.assertIn('1', counts)

    def test_quantum_circuit_multiple_qubits(self):
        # Create a more complex quantum circuit with multiple qubits
        qc = QuantumCircuit(2, 2)
        qc.h(0)  # Apply Hadamard gate to qubit 0
        qc.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
        qc.measure([0, 1], [0, 1])  # Measure both qubits

        # Visualize the quantum circuit results
        plot_results(qc, filename="entangled_circuit_histogram.png")

        # Execute the circuit on the AerSimulator
        result = self.simulator.run(qc).result()
        counts = result.get_counts(qc)

        # Check that the result is as expected (entangled state)
        self.assertIn('00', counts)
        self.assertIn('11', counts)

    def test_plot_statevector(self):
        # Create a quantum circuit to visualize the statevector
        qc = QuantumCircuit(1)
        qc.h(0)  # Apply Hadamard gate

        # Add the save_statevector instruction
        qc.save_statevector()

        # Visualize the statevector
        plot_statevector(qc, filename="statevector.png")

        # Execute the circuit on the AerSimulator
        result = self.simulator.run(qc).result()
        statevector = result.get_statevector(qc)

        # Check that the statevector is as expected (superposition state)
        self.assertAlmostEqual(abs(statevector[0])**2, 0.5, delta=0.1)
        self.assertAlmostEqual(abs(statevector[1])**2, 0.5, delta=0.1)

if __name__ == "__main__":
    unittest.main()