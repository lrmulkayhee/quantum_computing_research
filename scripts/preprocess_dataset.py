import pandas as pd
import json
import sys
import os
import re

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.data_processing import parse_parameters
from utils.helper_functions import normalize_vector

# Load the dataset
df = pd.read_csv('data/raw/dataset.csv')

# Inspect the parameters column
print(df['parameters'].head())

def parse_parameters(parameters):
    """
    Parse the parameters column from a string to a dictionary.
    
    Args:
        parameters (str): The parameters as a string.
        
    Returns:
        dict: The parameters as a dictionary.
    """
    try:
        # Replace single quotes with double quotes
        parameters = parameters.replace("'", '"')
        
        # Ensure keys are quoted
        parameters = re.sub(r'(\w+):', r'"\1":', parameters)
        
        # Attempt to load the string
        return json.loads(parameters)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Problematic string: {parameters}")
        return {}

def filter_numerical_values(d):
    """
    Filter out non-numerical values from a dictionary.
    
    Args:
        d (dict): The dictionary to filter.
        
    Returns:
        list: A list of numerical values.
    """
    return [v for v in d.values() if isinstance(v, (int, float))]

# Preprocess the dataset
def preprocess_dataset(df):
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert the parameters column to a dictionary
    df['parameters'] = df['parameters'].apply(parse_parameters)
    
    # Extract numerical values for normalization
    df['normalized_parameters'] = df['parameters'].apply(lambda x: normalize_vector(filter_numerical_values(x)))
    
    return df

# Preprocess the dataset
preprocessed_df = preprocess_dataset(df)

# Save the preprocessed data
preprocessed_df.to_pickle('data/preprocessed/preprocessed_data.pkl')
preprocessed_df.to_csv('data/preprocessed/preprocessed_data.csv', index=False)

print("Preprocessing complete. Preprocessed data saved to 'data/preprocessed/preprocessed_data.pkl' and 'data/preprocessed/preprocessed_data.csv'.")