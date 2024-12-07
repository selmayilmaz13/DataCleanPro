import pandas as pd
class Transformation:
    def __init__(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input data needs to be pandas DataFrame.")
        self.data = data

    def normalize_data(self, columns=None):
        """
        Normalize selected columns using Min-Max scaling.
        If no columns are specified, all numeric columns will be used.
        """
        if columns is None:
            columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        else:
            for col in columns:
                if col not in self.data.columns:
                    raise ValueError(f"Column '{col}' not found in the DataFrame.")

        if len(columns) == 0:
            raise ValueError("No numeric columns found or specified for normalization.")

        normalized_data = self.data.copy()
        for col in columns:
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                raise TypeError(f"Column '{col}' is not numeric. Cannot apply normalization.")
            min_value = self.data[col].min()
            max_value = self.data[col].max()
            if min_value == max_value:
                raise ValueError(f"Cannot normalize column '{col}' as it has a constant value.")
            normalized_data[col] = (self.data[col] - min_value) / (max_value - min_value)
        
        return normalized_data

    def standardize_data(self, columns=None):
        """
        Standardize selected columns using Z-score scaling.
        If no columns are specified, all numeric columns will be used.
        """
        if columns is None:
            columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        else:
            for col in columns:
                if col not in self.data.columns:
                    raise ValueError(f"Column '{col}' not found in the DataFrame.")

        if len(columns) == 0:
            raise ValueError("No numeric columns found or specified for standardization.")

        standardized_data = self.data.copy()
        for col in columns:
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                raise TypeError(f"Column '{col}' is not numeric. Cannot apply standardization.")
            mean = self.data[col].mean()
            std = self.data[col].std()
            if std == 0:
                raise ValueError(f"Cannot standardize column '{col}' as it has zero standard deviation.")
            standardized_data[col] = (self.data[col] - mean) / std
        
        return standardized_data