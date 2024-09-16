# Utility Functions

This folder contains utility functions and helper scripts that support the main algorithms and other functionalities of the project.

## Available Utilities

1. **Visualization** (`visualization.py`): Functions for visualizing quantum circuits and results.
2. **State Preparation** (`state_preparation.py`): Functions for preparing common quantum states like Bell and GHZ states.

## Usage

### Visualization

To plot the results of a quantum circuit:

```python
from utils.visualization import plot_results
plot_results(your_quantum_circuit)

To plot the statevector of a quantum circuit:
```python
from utils.visualization import plot_statevector
plot_statevector(your_quantum_circuit)

### State Preparation

To create a Bell state:

from utils.state_preparation import create_bell_state
bell_circuit = create_bell_state()

To create a GHZ state:

from utils.state_preparation import create_ghz_state
ghz_circuit = create_ghz_state(num_qubits=3)


