# DataCleanPro
Python-based toolkit for data processing and visualization. This project supports multiple data formats (`.csv`, `.xlsx`, `.json`) and includes methods for handling missing values, detecting outliers and creating visualizations.
## **Package Organization**

The package is organized into the following modules:

### **Data Handling**
- `DataLoader`: The first step in any data analysis or machine learning pipeline is loading the data. The DataLoader class in DataCleanPro allows users to load data from a variety of common file formats, such as CSV, JSON, and Excel.

### **Preprocessing**
- `Preprocessor`: Once the data is loaded, it usually needs to be cleaned and preprocessed before analysis. The Preprocessor class in DataCleanPro handles several common preprocessing tasks, such as handling missing values, encoding categorical variables, detecting outliers and removing duplicates.

### **Transformation**
- `Transformation`: After preprocessing, we may need to transform the data for machine learning models. This could involve standardizing or normalizing the data. The Transformation class provides methods for both operations.

### **Visualization**
- `Visualization`: To better understand the data and inspect the impact of preprocessing and transformations, DataCleanPro also offers basic data visualization tools using the Visualization class which creates insightful plots.
  

---

## **Features**

### **Data Handling**
- Supports loading data from `.csv`, `.xlsx`, and `.json` file formats with a single interface.

### **Preprocessing**
- Missing value handling: Imputation strategies (`mean`, `median`, `mode`) and drop.
- Outlier detection: Configurable methods (`Z-score`, `IQR`).
- Categorical encoding: `Label`, `One-hot`, and `Frequency` encoding.

### **Transformation**
- Normalize data using Min-Max scaling.
- Standardize data using Z-score scaling.
- Specify columns for transformation.

### **Visualization**
- Distribution plots
- Correlation heatmaps
- Boxplots for outliers
- Categorical count plots
- Grouped boxplots
- Histograms for numeric columns

---

## **Example Usage**

### **Loading Data**

Load data from different file formats:

```python
from toolkit import DataLoader

# Load CSV
csv_data = DataLoader.load_csv("https://example.com/data.csv")

# Load XLSX
xlsx_data = DataLoader.load_xlsx("https://example.com/data.xlsx")

# Load JSON
json_data = DataLoader.load_json("https://example.com/data.json")
