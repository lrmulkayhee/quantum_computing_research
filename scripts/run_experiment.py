import pandas as pd
import json
import os
import sys
import time
import matplotlib.pyplot as plt

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.grover import run_grover
from algorithms.qpe import run_qpe
from algorithms.shor import run_shor
from utils.state_preparation import prepare_state
from utils.helper_functions import create_superposition_state, measure_all

# Load the preprocessed dataset
train_df = pd.read_csv('data/preprocessed/preprocessed_data.csv')

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
        parameters = json.loads(row['parameters'].replace("'", '"'))
        
        # Prepare the state
        prepared_state = prepare_state(parameters)
        
        start_time = time.time()
        if problem_type == 'Search':
            result = run_grover(parameters)
            algorithm = 'Grover'
            accuracy = result.get('accuracy', None)
        elif problem_type == 'Phase Estimation':
            result = run_qpe(parameters)
            algorithm = 'QPE'
            accuracy = result.get('accuracy', None)
        elif problem_type == 'Factorization':
            result = run_shor(parameters) # Pass parameters instead of prepared_state
            algorithm = 'Shor'
            accuracy = result.get('accuracy', None)
        
        execution_time = time.time() - start_time
        
        # Example usage of helper functions
        superposition_circuit = create_superposition_state(len(parameters))
        measured_circuit = measure_all(superposition_circuit)
        
        # Convert tuple result to dictionary
        if isinstance(result, tuple):
            result_dict = {'factor1': result[0], 'factor2': result[1]}
        else:
            result_dict = result
        
        result_dict.update({
            'algorithm': algorithm,
            'execution_time': execution_time,
            'accuracy': accuracy
        })
        
        results.append(result_dict)
    
    results_df = pd.DataFrame(results)
    results_df.to_csv('experiments/results/tables/results_table.csv', index=False)
    
    # Example: Save a report
    with open('experiments/results/reports/experiment_report.md', 'w') as f:
        f.write("# Experiment Report\n")
        f.write("This is a sample report for the experiment.\n")
    
    print("Experiment complete. Results saved in the 'experiments' folder.")

# Run the experiment
run_experiment(train_df)