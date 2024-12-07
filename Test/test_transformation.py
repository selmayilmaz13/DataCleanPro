import pandas as pd
from transformation import Transformation
from data_loader import DataLoader

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dl = DataLoader()
data = dl.load_csv(url)

# Initialize the Transformation class
transformer = Transformation(data)

# Normalize specific columns (e.g., 'Age' and 'Fare')
try:
    normalized_data = transformer.normalize_data(columns=['Age', 'Fare'])
    print("\nNormalized Data (Age, Fare):")
    print(normalized_data[['Age', 'Fare']].head())  # Display only transformed columns
except Exception as e:
    print(f"\nError during normalization: {e}")

# Standardize specific columns (e.g., 'Age' and 'Fare')
try:
    standardized_data = transformer.standardize_data(columns=['Age', 'Fare'])
    print("\nStandardized Data (Age, Fare):")
    print(standardized_data[['Age', 'Fare']].head())  # Display only transformed columns
except Exception as e:
    print(f"\nError during standardization: {e}")
