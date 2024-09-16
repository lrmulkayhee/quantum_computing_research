import pandas as pd
import json
import os
import matplotlib.pyplot as plt

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
    summary = df.groupby('algorithm').agg({
        'execution_time': 'mean',
        'accuracy': 'mean'
    }).reset_index()
    
    # Save the summary table
    summary.to_csv('experiments/results/tables/summary_statistics.csv', index=False)
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(summary['algorithm'], summary['execution_time'], color='blue', alpha=0.7, label='Execution Time')
    plt.xlabel('Algorithm')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time by Algorithm')
    plt.legend()
    plt.savefig('experiments/results/figures/execution_time.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    plt.bar(summary['algorithm'], summary['accuracy'], color='green', alpha=0.7, label='Accuracy')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.title('Accuracy by Algorithm')
    plt.legend()
    plt.savefig('experiments/results/figures/accuracy.png')
    plt.close()
    
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