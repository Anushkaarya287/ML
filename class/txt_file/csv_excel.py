import pandas as pd


csv_data = pd.read_csv("university_records.csv")
print("\nCSV Data:\n", csv_data)


import os

if os.path.exists("sample.xlsx"):
    excel_data = pd.read_excel("sample.xlsx")
    print("\nExcel Data:\n", excel_data)
else:
    print("\nExcel file 'sample.xlsx' not found. Skipping Excel loading.")