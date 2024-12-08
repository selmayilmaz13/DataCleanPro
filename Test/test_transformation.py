from DataCleanPro import *


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dl = DataLoader()
data = dl.load_csv(url)


transformer = Transformation(data)


try:
    normalized_data = transformer.normalize_data(columns=['Age', 'Fare'])
    print("\nNormalized Data (Age, Fare):")
    print(normalized_data[['Age', 'Fare']].head()) 
except Exception as e:
    print(f"\nError during normalization: {e}")


try:
    standardized_data = transformer.standardize_data(columns=['Age', 'Fare'])
    print("\nStandardized Data (Age, Fare):")
    print(standardized_data[['Age', 'Fare']].head())  
except Exception as e:
    print(f"\nError during standardization: {e}")
