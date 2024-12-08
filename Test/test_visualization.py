from DataCleanPro import *

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dl = DataLoader()




viz = Visualization(dl.load_csv(url))


try:
   
    print("\nPlotting distribution of 'Age':")
    viz.plot_distribution('Age')
except Exception as e:
    print(f"Error: {e}")

try:
  
    print("\nPlotting outliers in 'Fare':")
    viz.plot_outliers('Fare')
except Exception as e:
    print(f"Error: {e}")

try:
   
    print("\nPlotting correlation heatmap:")
    viz.plot_correlation_heatmap()
except Exception as e:
    print(f"Error: {e}")

try:
  
    print("\nPlotting pairwise scatter plots:")
    viz.plot_pairwise_scatter()
except Exception as e:
    print(f"Error: {e}")

try:
   
    print("\nPlotting count of categories in 'Embarked':")
    viz.plot_categorical_count('Embarked')
except Exception as e:
    print(f"Error: {e}")

try:
  
    print("\nPlotting distribution of 'Age' by 'Pclass':")
    viz.plot_distribution_by_category('Age', 'Pclass')
except Exception as e:
    print(f"Error: {e}")

try:
    
    print("\nPlotting grouped boxplot of 'Fare' by 'Pclass':")
    viz.plot_grouped_boxplot('Fare', 'Pclass')
except Exception as e:
    print(f"Error: {e}")

try:
   
    print("\nPlotting histograms for all numeric columns:")
    viz.plot_histograms()
except Exception as e:
    print(f"Error: {e}")
