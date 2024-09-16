import pandas as pd
import json
import sys
import os

# Add src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils.data_processing import parse_parameters
from utils.helperfunctions import normalize_vector  # Example import

# Load the dataset
df = pd.read_csv('data/raw/dataset.csv')

# Preprocess the dataset
def preprocess_dataset(df):
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert the parameters column to a dictionary
    df['parameters'] = df['parameters'].apply(parse_parameters)
    
    # Example usage of a helper function
    df['normalized_parameters'] = df['parameters'].apply(normalize_vector)
    
    return df

# Preprocess the dataset
preprocessed_df = preprocess_dataset(df)

# Save the preprocessed data
preprocessed_df.to_pickle('data/preprocessed/preprocessed_data.pkl')
preprocessed_df.to_csv('data/preprocessed/preprocessed_data.csv', index=False)

print("Preprocessing complete. Preprocessed data saved to 'data/preprocessed/preprocessed_data.pkl' and 'data/preprocessed/preprocessed_data.csv'.")