import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Add the directory containing metrics.py to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src', 'utils'))

# Import the functions from metrics.py
from metrics import calculate_summary_statistics

# Load the results
results_df = pd.read_csv('experiments/results/tables/results_table.csv')

# Print the columns to inspect the available data
print("Columns in results_df:", results_df.columns)

# Check if the necessary columns exist
required_columns = ['algorithm', 'execution_time', 'accuracy', 'factor1', 'factor2']
missing_columns = [col for col in required_columns if col not in results_df.columns]
if missing_columns:
    print(f"Missing columns in results_df: {missing_columns}")
else:
    # Print a sample of the data
    print("Sample data from results_df:")
    print(results_df.head())

    # Check for NaN values
    print("Checking for NaN values in execution_time and accuracy columns:")
    print(results_df[['execution_time', 'accuracy']].isna().sum())

    # Drop rows with NaN values in execution_time or accuracy
    results_df = results_df.dropna(subset=['execution_time', 'accuracy'])

    # Filter out Shor's algorithm from the results
    filtered_df = results_df[results_df['algorithm'] != 'Shor']

    # Plot execution time vs accuracy for each algorithm (excluding Shor)
    algorithms = filtered_df['algorithm'].unique()
    plt.figure(figsize=(10, 6))
    for algo in algorithms:
        subset = filtered_df[filtered_df['algorithm'] == algo]
        if not subset.empty:
            print(f"Plotting data for algorithm: {algo}")
            print(subset[['execution_time', 'accuracy']].head())
            plt.scatter(subset['execution_time'], subset['accuracy'], label=algo)
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Accuracy')
    plt.title('Execution Time vs Accuracy for Different Algorithms (Excluding Shor)')
    plt.legend()
    plt.savefig('experiments/results/figures/execution_time_vs_accuracy.png')
    plt.show()
    plt.close()  # Close the figure

    # Plot histograms of the factors for Shor's algorithm
    shor_results = results_df[results_df['algorithm'] == 'Shor']
    if not shor_results.empty:
        plt.figure(figsize=(10, 5))
        shor_results[['factor1', 'factor2']].hist(bins=20, figsize=(10, 5))
        plt.suptitle('Distribution of Factors (Shor\'s Algorithm)')
        plt.savefig('experiments/results/figures/factors_distribution.png')
        plt.show()
        plt.close()  # Close the figure

    # Calculate and display summary statistics
    summary_stats = calculate_summary_statistics(results_df)
    print("Summary Statistics:")
    print(summary_stats)

    # Save a summary report
    with open('experiments/results/reports/summary_report.md', 'w') as f:
        f.write("# Summary Report\n")
        f.write("This is a summary report of the experiment results.\n")
        f.write(f"Total experiments: {len(results_df)}\n")
        for algo in algorithms:
            subset = results_df[results_df['algorithm'] == algo]
            f.write(f"\n## {algo} Algorithm\n")
            f.write(f"Total runs: {len(subset)}\n")
            if 'accuracy' in subset.columns:
                f.write(f"Average accuracy: {subset['accuracy'].mean()}\n")
            if 'execution_time' in subset.columns:
                f.write(f"Average execution time: {subset['execution_time'].mean()}\n")
        if not shor_results.empty:
            f.write("\n## Shor's Algorithm Factors\n")
            f.write(f"Factor 1 - Mean: {shor_results['factor1'].mean()}, Std: {shor_results['factor1'].std()}\n")
            f.write(f"Factor 2 - Mean: {shor_results['factor2'].mean()}, Std: {shor_results['factor2'].std()}\n")
        f.write("\n## Summary Statistics\n")
        f.write(summary_stats.to_markdown())

    print("Analysis complete. Summary report saved in the 'experiments/results/reports' folder.")