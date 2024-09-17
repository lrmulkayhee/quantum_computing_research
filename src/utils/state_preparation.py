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

def prepare_state(parameters):
    """
    Prepare the quantum state based on the given parameters.
    
    Args:
        parameters (dict): The parameters for state preparation.
        
    Returns:
        QuantumCircuit: The prepared quantum circuit.
    """
    state_type = parameters.get('state_type', 'bell')
    num_qubits = parameters.get('num_qubits', 2)
    
    if state_type == 'bell':
        return create_bell_state()
    elif state_type == 'ghz':
        return create_ghz_state(num_qubits)
    else:
        raise ValueError(f"Unknown state type: {state_type}")