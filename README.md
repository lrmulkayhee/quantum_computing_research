# Quantum Computing Research Project

This repository contains code and documentation for a quantum computing research project focused on testing NIST encryption tools.

## Table of Contents

1. [Setup](#setup)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Algorithms](#algorithms)
5. [Utilities](#utilities)
6. [License](#license)

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/quantum-computing-research.git
   cd quantum-computing-research
2. Create and activate a virtual environment:
   ```sh
   python -m venv quantum_env
   quantum_env\Scripts\activate  # On Windows
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt

## Usage

Run the encryption test script:

```sh
python src/algorithms/encryption_test.py
```

## Project Structure

quantum-computing-research/
├── docs/
│   ├── index.md
├── notebooks/
│   ├── introduction.ipynb
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── visualization.py
│   │   ├── state_preparation.py
│   │   ├── helper_functions.py
│   │   └── readme.md
│   ├── algorithms/
│   │   ├── encryption_test.py
│   │   ├── grover.py
│   │   ├── shor.py
│   │   ├── qpe.py
│   │   └── test_encryption_test.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## Algorithms

This folder contains implementations of various quantum algorithms used in this research project.

### Available Algorithms
1. Grover's Algorithm (grover.py): An algorithm for searching an unsorted database or an unstructured list.
2. Shor's Algorithm (shor.py): An algorithm for integer factorization, which can break RSA encryption.
3. Quantum Phase Estimation (QPE) (qpe.py): An algorithm for estimating the phase (eigenvalue) of an eigenvector of a unitary operator.

## Utilities

This folder contains utility functions and helper scripts that support the main algorithms and other functionalities of the project.

### Available Utilities
1. Visualization (visualization.py): Functions for visualizing quantum circuits and results.
2. State Preparation (state_preparation.py): Functions for preparing common quantum states like Bell and GHZ states.
3. Helper Functions (helper_functions.py): General-purpose utility functions.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

