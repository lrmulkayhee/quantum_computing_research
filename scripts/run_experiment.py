import pandas as pd
import json

# Load the dataset
df = pd.read_csv('data/raw/dataset.csv')

# Function to parse the parameters column
def parse_parameters(parameters):
    return json.loads(parameters.replace("'", '"'))

# Preprocess the dataset
def preprocess_dataset(df):
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert the parameters column to a dictionary
    df['parameters'] = df['parameters'].apply(parse_parameters)
    
    return df

# Preprocess the dataset
preprocessed_df = preprocess_dataset(df)

# Save the preprocessed data
preprocessed_df.to_pickle('data/preprocessed/preprocessed_data.pkl')
preprocessed_df.to_csv('data/preprocessed/preprocessed_data.csv', index=False)

print("Preprocessing complete. Preprocessed data saved to 'data/preprocessed/preprocessed_data.pkl' and 'data/preprocessed/preprocessed_data.csv'.")