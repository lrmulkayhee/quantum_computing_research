import pandas as pd
import json
import os
import sys
import matplotlib.pyplot as plt

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.metrics import calculate_summary_statistics
from utils.visualization import plot_results
from utils.helperfunctions import tensor_product  # Example import

# Load the preprocessed dataset
preprocessed_df = pd.read_pickle('data/preprocessed/preprocessed_data.pkl')

# Function to analyze the results
def analyze_results(df):
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
    
    # Group by algorithm and calculate mean execution time and accuracy
    summary = calculate_summary_statistics(df)
    
    # Example usage of a helper function
    tensor_product_result = tensor_product(summary['execution_time'].values, summary['accuracy'].values)
    
    # Save the summary table
    summary.to_csv('experiments/results/tables/summary_statistics.csv', index=False)
    
    # Plot the results using the visualization utility
    plot_results(summary, 'experiments/results/figures/')
    
    # Example: Save a report
    with open('experiments/results/reports/experiment_report.md', 'w') as f:
        f.write("# Experiment Report\n")
        f.write("## Summary Statistics\n")
        f.write(summary.to_markdown(index=False))
        f.write("\n\n")
        f.write("## Figures\n")
        f.write("![Execution Time](../figures/execution_time.png)\n")
        f.write("![Accuracy](../figures/accuracy.png)\n")
    
    print("Analysis complete. Results saved in the 'experiments' folder.")

# Analyze the results
analyze_results(preprocessed_df)