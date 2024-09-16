from qiskit import QuantumCircuit

def create_bell_state():
    """Create a Bell state."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    return qc

def create_ghz_state(num_qubits):
    """Create a GHZ state."""
    qc = QuantumCircuit(num_qubits)
    qc.h(0)
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
    return qc