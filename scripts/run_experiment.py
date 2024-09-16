import pandas as pd
import json
import os
import sys

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.grover import run_grover
from algorithms.qpe import run_qpe
from algorithms.shor import run_shor
from utils.state_preparation import prepare_state
from utils.helperfunctions import create_superposition_state, measure_all  # Example imports

# Load the preprocessed dataset
preprocessed_df = pd.read_pickle('data/preprocessed/preprocessed_data.pkl')

# Function to run an experiment
def run_experiment(df):
    # Create directories for experiment results
    os.makedirs('experiments/configs', exist_ok=True)
    os.makedirs('experiments/logs', exist_ok=True)
    os.makedirs('experiments/results/figures', exist_ok=True)
    os.makedirs('experiments/results/tables', exist_ok=True)
    os.makedirs('experiments/results/reports', exist_ok=True)
    
    # Example: Save a configuration file
    config = {
        'experiment_name': 'Quantum Algorithm Benchmarking',
        'date': '2023-10-01'
    }
    with open('experiments/configs/config.json', 'w') as f:
        json.dump(config, f)
    
    # Example: Save a log file
    with open('experiments/logs/experiment_log.txt', 'w') as f:
        f.write("Experiment started...\n")
    
    # Example: Run algorithms and save results
    results = []
    for index, row in df.iterrows():
        problem_type = row['problem_type']
        parameters = row['parameters']
        
        # Prepare the state
        prepared_state = prepare_state(parameters)
        
        if problem_type == 'Search':
            result = run_grover(prepared_state)
        elif problem_type == 'Phase Estimation':
            result = run_qpe(prepared_state)
        elif problem_type == 'Factorization':
            result = run_shor(prepared_state)
        
        # Example usage of helper functions
        superposition_circuit = create_superposition_state(len(parameters))
        measured_circuit = measure_all(superposition_circuit, len(parameters))
        
        results.append(result)
    
    results_df = pd.DataFrame(results)
    results_df.to_csv('experiments/results/tables/results_table.csv', index=False)
    
    # Example: Save a report
    with open('experiments/results/reports/experiment_report.md', 'w') as f:
        f.write("# Experiment Report\n")
        f.write("This is a sample report for the experiment.\n")
    
    print("Experiment complete. Results saved in the 'experiments' folder.")

# Run the experiment
run_experiment(preprocessed_df)