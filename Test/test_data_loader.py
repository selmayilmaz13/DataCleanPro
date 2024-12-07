from data_loader import DataLoader


csv_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
xlsx_url ='http://www.econ.yale.edu/~shiller/data/chapt26.xls'
json_url = "https://jsonplaceholder.typicode.com/posts"


dl = DataLoader()


try:
    csv_data = dl.load_csv(csv_url)
    print("\nCSV Data Loaded:")
    print(csv_data.head())
except Exception as e:
    print(f"\nError loading CSV: {e}")


try:
    xlsx_data = dl.load_xlsx(xlsx_url)
    print("\nXLSX Data Loaded:")
    print(xlsx_data.head())
except Exception as e:
    print(f"\nError loading XLSX: {e}")

try:
    json_data = dl.load_json(json_url)
    print("\nJSON Data Loaded:")
    print(json_data.head())
except Exception as e:
    print(f"\nError loading JSON: {e}")
