import json
import pandas as pd
import re

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
        
        # Attempt to load the JSON string
        return json.loads(parameters)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Problematic string: {parameters}")
        return {}

def clean_data(df):
    """
    Clean the dataset by dropping rows with missing values and parsing parameters.
    
    Args:
        df (pd.DataFrame): The raw dataset.
        
    Returns:
        pd.DataFrame: The cleaned dataset.
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert the parameters column to a dictionary
    df['parameters'] = df['parameters'].apply(parse_parameters)
    
    return df

def normalize_column(df, column_name):
    """
    Normalize a specified column in the dataframe.
    
    Args:
        df (pd.DataFrame): The dataset.
        column_name (str): The name of the column to normalize.
        
    Returns:
        pd.DataFrame: The dataset with the normalized column.
    """
    df[column_name] = (df[column_name] - df[column_name].mean()) / df[column_name].std()
    return df

def split_dataset(df, test_size=0.2):
    """
    Split the dataset into training and testing sets.
    
    Args:
        df (pd.DataFrame): The dataset.
        test_size (float): The proportion of the dataset to include in the test split.
        
    Returns:
        tuple: The training and testing datasets.
    """
    train_df = df.sample(frac=1 - test_size, random_state=42)
    test_df = df.drop(train_df.index)
    return train_df, test_df