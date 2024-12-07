import pandas as pd


class Preprocessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

   
    def check_missing_values(self):
        """Print missing values per column."""
        missing= self.data.isnull().sum()
        if missing.empty:
            print("No missing values found.")
        else:
            print("Missing Values:\n", missing)
        

    def handle_missing_values(self, strategy="mean"):
        """Handle missing values by mean, median, mode, or drop."""
        valid = ["mean", "median", "mode", "drop"]
        if strategy not in valid:
            raise ValueError(f"Invalid encoding '{strategy}'. Valid are: {valid}.")

        if strategy == "mean":
            for col in self.data.columns:
                if self.data[col].dtype in ['int64', 'float64']:
                    self.data[col] = self.data[col].fillna(self.data[col].mean())
        elif strategy == "median":
            for col in self.data.columns:
                if self.data[col].dtype in ['int64', 'float64']:
                    self.data[col] = self.data[col].fillna(self.data[col].median())
        elif strategy == 'mode':
            for col in self.data.columns:
                mode_val = self.data[col].mode(dropna=True)
                if not mode_val.empty:
                    self.data[col] = self.data[col].fillna(mode_val.iloc[0])
        elif strategy == "drop":
            self.data = self.data.dropna()
       
        return self.data

   
    def encode_categorical(self, columns, method="label", order=None):
        """Encode categorical variables with one method at a time:
        - label: Label encoding
        - onehot: One-hot encoding
        - frequency: Frequency encoding"""
        if not columns:
            raise ValueError("No columns provided.")
        valid = ["label", "onehot", "frequency"]
        for col in columns:
            if col not in self.data.columns:
                raise ValueError(f"Column '{col}' not found.")
           
            if not (pd.api.types.is_object_dtype(self.data[col]) or pd.api.types.is_categorical_dtype(self.data[col])):
                raise TypeError(f"Column '{col}' is not categorical. Categorical columns only.")

        if method not in valid:
            raise ValueError(f"Invalid encoding '{method}'. Valid are: {valid}.")

        if method == "label":
            for col in columns:
                if col in self.data.columns:
                    categories = self.data[col].astype(str).unique()
                    category_map = {category: index for index, category in enumerate(categories)}
                    self.data[col] = self.data[col].map(category_map)

        elif method == "onehot":
            self.data = pd.get_dummies(self.data, columns=columns)

        elif method == "frequency":
            for col in columns:
                if col in self.data.columns:
                    freq = self.data[col].value_counts(dropna=False)
                    freq_i = freq / freq.sum()
                    self.data[col] = self.data[col].map(freq_i)

        
        return self.data

  
    def handle_outliers(self, columns=None, method="iqr", threshold=1.5, zscore_threshold=3.0, remove=False, visualize=False):
        """
        Detect (or remove) outliers using either IQR or Z-score method.
        method: 'iqr' or 'zscore'
        threshold: used for IQR method
        zscore_threshold: used for Z-score method
        remove: if True, remove outliers; if False, just return them
        """
        if columns is None:
            columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        valid = ["iqr", "zscore"]
        if method not in valid:
            raise ValueError(f"Invalid method '{method}'. Valid are: {valid}.")

        if columns is None:
            columns = self.data.select_dtypes(include=['int64', 'float64']).columns
            if len(columns) == 0:
                raise ValueError("No numeric columns found for outlier detection.")
        outliers_index = set() #unique id's
        if method == "iqr":
            for col in columns:
                q1 = self.data[col].quantile(0.25)
                q3 = self.data[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - threshold * iqr
                upper_bound = q3 + threshold * iqr
                col_outliers = self.data[(self.data[col] < lower_bound) | (self.data[col] > upper_bound)].index
                outliers_index.update(col_outliers)
                
        elif method == "zscore":
            numeric_columns = self.data[columns]
            mean = numeric_columns.mean()
            std = numeric_columns.std(ddof=0)
            z_score = (numeric_columns - mean) / std
            filter = (z_score.abs() > zscore_threshold).any(axis=1)
            col_outliers = self.data[filter].index
            outliers_index.update(col_outliers)
        else:
            raise ValueError("Invalid method. Choose 'iqr' or 'zscore'.")
        outliers_index = list(outliers_index)
        outliers_df = self.data.loc[outliers_index]


        if remove:
            self.data = self.data.drop(index=outliers_index)
            return self.data
        else:
            return outliers_df

   
  

    def check_duplicates(self, subset=None):
        """Check if duplicates exist without removing them."""
        dup_count = self.data.duplicated(subset=subset).sum()
        print(f"Number of duplicate rows: {dup_count}")
        return dup_count

    def remove_duplicates(self, subset=None, keep='first'):
        """Remove duplicates"""
        dup_count = self.check_duplicates(subset)
        self.data = self.data.drop_duplicates(subset=subset, keep=keep)
        return self.data
