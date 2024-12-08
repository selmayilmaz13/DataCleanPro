import unittest
import pandas as pd
import matplotlib.pyplot as plt
from DataCleanPro import *

class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        dl = DataLoader()
        data = dl.load_csv(url)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)

    def test_load_xlsx(self):
        url = 'http://www.econ.yale.edu/~shiller/data/chapt26.xlsx'
        dl = DataLoader()
        data = dl.load_xlsx(url) 
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)

    def test_load_json(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        dl = DataLoader()
        data = dl.load_json(url)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)

class TestPreprocessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        dl = DataLoader()
        cls.data = dl.load_csv(url)
        cls.preprocessor = Preprocessor(cls.data)

    def test_handle_missing_values(self):
        self.preprocessor.handle_missing_values(strategy="mode")
        self.assertEqual(self.preprocessor.data.isnull().sum().sum(), 0)

    def test_encode_categorical(self):
        self.preprocessor.encode_categorical(columns=["Sex", "Embarked"], method="frequency")
        self.assertIn("Sex", self.preprocessor.data.columns)
        self.assertIn("Embarked", self.preprocessor.data.columns)

    def test_handle_outliers(self):
        outliers = self.preprocessor.handle_outliers(method="iqr", remove=False)
        self.assertIsInstance(outliers, pd.DataFrame)
        self.preprocessor.handle_outliers(method="iqr", remove=True)
        self.assertLess(len(self.preprocessor.data), len(self.data))

    def test_remove_duplicates(self):
        self.preprocessor.remove_duplicates()
        self.assertEqual(self.preprocessor.data.duplicated().sum(), 0)

class TestTransformation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        dl = DataLoader()
        cls.data = dl.load_csv(url)
        cls.transformer = Transformation(cls.data)

    def test_normalize_data(self):
        #test fails because the missing values are not removed
        #if we exclude missing values it would work
        normalized_data = self.transformer.normalize_data(columns=['Age', 'Fare'])
        self.assertIn('Age', normalized_data.columns)
        self.assertIn('Fare', normalized_data.columns)
        self.assertTrue((normalized_data['Age'] >= 0).all() and (normalized_data['Age'] <= 1).all())
        self.assertTrue((normalized_data['Fare'] >= 0).all() and (normalized_data['Fare'] <= 1).all())

    def test_standardize_data(self):
        standardized_data = self.transformer.standardize_data(columns=['Age', 'Fare'])
        self.assertIn('Age', standardized_data.columns)  
        self.assertIn('Fare', standardized_data.columns)
        self.assertAlmostEqual(standardized_data['Age'].mean(), 0, places=5)
        self.assertAlmostEqual(standardized_data['Age'].std(), 1, places=5)
        self.assertAlmostEqual(standardized_data['Fare'].mean(), 0, places=5)
        self.assertAlmostEqual(standardized_data['Fare'].std(), 1, places=5)

class TestVisualization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        dl = DataLoader()
        cls.data = dl.load_csv(url)
        cls.viz = Visualization(cls.data)

    def test_plot_distribution(self):
        self.viz.plot_distribution('Age')
        self.assertTrue(plt.gcf().number)  # Assert that a plot was created

    def test_plot_outliers(self):
        self.viz.plot_outliers('Fare')
        self.assertTrue(plt.gcf().number)

    def test_plot_correlation_heatmap(self):
        self.viz.plot_correlation_heatmap()
        self.assertTrue(plt.gcf().number)  

    def test_plot_categorical_count(self):
        self.viz.plot_categorical_count('Embarked')
        self.assertTrue(plt.gcf().number)
    
    def test_plot_distribution_by_category(self):  
        self.viz.plot_distribution_by_category('Age', 'Embarked')
        self.assertTrue(plt.gcf().number)

    def test_plot_grouped_boxplot(self):
        self.viz.plot_grouped_boxplot('Fare', 'Embarked') 
        self.assertTrue(plt.gcf().number)

    def test_plot_histograms(self):
        self.viz.plot_histograms()
        self.assertTrue(plt.gcf().number)

if __name__ == '__main__':
    unittest.main()