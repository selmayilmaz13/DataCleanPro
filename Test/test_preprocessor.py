from DataCleanPro import *

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dl = DataLoader()








pre = Preprocessor( dl.load_csv(url))


print("\nChecking Missing Values:")
pre.check_missing_values()


pre.handle_missing_values(strategy="mode")
print(pre.data)


print("\nEncoding Categorical Columns using frequency encoding:")
pre.encode_categorical(columns=["Sex", "Embarked"], method="frequency")
print(pre.data)


print("\nDetecting Outliers with IQR method (not removing):")
outliers = pre.handle_outliers(method="iqr", remove=False)
print("Outliers detected:")
print(outliers)

print("\nRemoving Outliers:")
pre.handle_outliers(method="iqr", remove=True)
print(pre.data)


print("\nChecking for Duplicates:")
pre.check_duplicates()

print("\nRemoving Duplicates:")
pre.remove_duplicates()
print(pre.data)
