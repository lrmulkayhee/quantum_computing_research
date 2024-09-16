import pandas as pd
import numpy as np

def calculate_summary_statistics(df):
    """
    Calculate summary statistics for the dataset.
    
    Args:
        df (pd.DataFrame): The dataset containing results.
        
    Returns:
        pd.DataFrame: A dataframe with summary statistics.
    """
    summary = df.groupby('algorithm').agg({
        'execution_time': ['mean', 'std', 'min', 'max'],
        'accuracy': ['mean', 'std', 'min', 'max']
    }).reset_index()
    
    # Flatten the multi-level columns
    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    summary.rename(columns={'algorithm_': 'algorithm'}, inplace=True)
    
    return summary

def calculate_accuracy(predictions, targets):
    """
    Calculate the accuracy of predictions.
    
    Args:
        predictions (np.array): The predicted values.
        targets (np.array): The true values.
        
    Returns:
        float: The accuracy of the predictions.
    """
    return np.mean(predictions == targets)

def calculate_execution_time(start_time, end_time):
    """
    Calculate the execution time of an algorithm.
    
    Args:
        start_time (float): The start time.
        end_time (float): The end time.
        
    Returns:
        float: The execution time.
    """
    return end_time - start_time

def calculate_confusion_matrix(predictions, targets):
    """
    Calculate the confusion matrix for binary classification.
    
    Args:
        predictions (np.array): The predicted values.
        targets (np.array): The true values.
        
    Returns:
        np.array: The confusion matrix.
    """
    tp = np.sum((predictions == 1) & (targets == 1))
    tn = np.sum((predictions == 0) & (targets == 0))
    fp = np.sum((predictions == 1) & (targets == 0))
    fn = np.sum((predictions == 0) & (targets == 1))
    
    return np.array([[tn, fp], [fn, tp]])

def calculate_precision_recall_f1(predictions, targets):
    """
    Calculate precision, recall, and F1 score for binary classification.
    
    Args:
        predictions (np.array): The predicted values.
        targets (np.array): The true values.
        
    Returns:
        tuple: Precision, recall, and F1 score.
    """
    tp = np.sum((predictions == 1) & (targets == 1))
    fp = np.sum((predictions == 1) & (targets == 0))
    fn = np.sum((predictions == 0) & (targets == 1))
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1