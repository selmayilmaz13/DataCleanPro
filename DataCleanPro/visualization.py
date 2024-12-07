import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
class Visualization:
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data must be a pandas DataFrame.")
        self.data = data

    def plot_distribution(self, column):
        """Plots the distribution of a given column."""
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.data[column]):
            raise TypeError(f"Column '{column}' is not numeric. Distribution plots require numeric data.")
        
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_outliers(self, column):
        """Plots a boxplot to detect outliers in a given column."""
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.data[column]):
            raise TypeError(f"Column '{column}' is not numeric. Boxplots require numeric data.")
        
        sns.boxplot(x=self.data[column])
        plt.title(f'Outliers in {column}')
        plt.show()

    def plot_correlation_heatmap(self):
        """Plots a heatmap of correlations between numeric features."""
        numeric_data = self.data.select_dtypes(include=['int64', 'float64'])
        if numeric_data.empty:
            raise ValueError("No numeric columns found in the DataFrame for correlation heatmap.")
        
        correlation_matrix = numeric_data.corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.show()

    # def plot_pairwise_scatter(self):
    #     """Plots pairwise scatter plots for numeric features."""
    #     numeric_data = self.data.select_dtypes(include=['int64', 'float64'])
    #     if numeric_data.empty:
    #         raise ValueError("No numeric columns found in the DataFrame for pairwise scatter plots.")
        
    #     sns.pairplot(numeric_data)
    #     plt.suptitle('Pairwise Scatter Plot', y=1.02)  # Adjust title position
    #     plt.show()

    def plot_categorical_count(self, column):
        """Plots the count of each category in a categorical column."""
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame.")
        if not pd.api.types.is_categorical_dtype(self.data[column]) and not pd.api.types.is_object_dtype(self.data[column]):
            raise TypeError(f"Column '{column}' is not categorical. Count plots require categorical data.")
        
        sns.countplot(x=self.data[column])
        plt.title(f'Count of Categories in {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.show()

    def plot_distribution_by_category(self, column, category):
        """Plots the distribution of a numeric column grouped by a categorical column."""
        if column not in self.data.columns or category not in self.data.columns:
            raise ValueError(f"Column '{column}' or '{category}' not found in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.data[column]):
            raise TypeError(f"Column '{column}' is not numeric. Distribution plots require numeric data.")
        if not pd.api.types.is_categorical_dtype(self.data[category]) and not pd.api.types.is_object_dtype(self.data[category]):
            raise TypeError(f"Column '{category}' is not categorical. Grouped distributions require categorical grouping.")
        
        sns.FacetGrid(self.data, hue=category, height=6).map(sns.histplot, column, kde=True).add_legend()
        plt.title(f'Distribution of {column} by {category}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_grouped_boxplot(self, numeric_column, category_column):
        """Plots a boxplot of a numeric column grouped by a categorical column."""
        if numeric_column not in self.data.columns or category_column not in self.data.columns:
            raise ValueError(f"Column '{numeric_column}' or '{category_column}' not found in the DataFrame.")
        if not pd.api.types.is_numeric_dtype(self.data[numeric_column]):
            raise TypeError(f"Column '{numeric_column}' is not numeric. Boxplots require numeric data.")
        if not pd.api.types.is_categorical_dtype(self.data[category_column]) and not pd.api.types.is_object_dtype(self.data[category_column]):
            raise TypeError(f"Column '{category_column}' is not categorical. Grouped boxplots require categorical grouping.")
        
        sns.boxplot(x=category_column, y=numeric_column, data=self.data)
        plt.title(f'Boxplot of {numeric_column} by {category_column}')
        plt.xlabel(category_column)
        plt.ylabel(numeric_column)
        plt.xticks(rotation=45)
        plt.show()

    def plot_histograms(self):
        """Plots histograms for all numeric columns."""
        numeric_columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_columns) == 0:
            raise ValueError("No numeric columns found in the DataFrame for histograms.")
        
        self.data[numeric_columns].hist(figsize=(12, 10), bins=20)
        plt.suptitle('Histograms of Numeric Columns', fontsize=16)
        plt.show()
