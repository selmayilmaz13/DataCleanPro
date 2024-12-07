
import pandas as pd

class DataLoader:
    @staticmethod
    def load_csv(file_path):
        """Load a CSV file from a URL or local path into a DataFrame."""
        return pd.read_csv(file_path)
    @staticmethod
    def load_xlsx(file_path):
        """Load a XLSX file from a URL or local path into a DataFrame."""
        return pd.read_excel(file_path,'sheetname')
    @staticmethod
    def load_json(file_path):
        """Load a JSON file from a URL or local path into a DataFrame."""
        return pd.read_json(file_path)