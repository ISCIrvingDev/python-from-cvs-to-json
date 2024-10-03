import csv
import json
import pandas as pd

CSV_PATH = "./src/csvs/data.csv" # Relative path from which the cmd was opened

data_csv = pd.read_csv(CSV_PATH)
print("CSV data:")
print(data_csv)

data_json = json.dumps(list(csv.reader(open(CSV_PATH, encoding="utf-8"))))
print("JSON data:")
print(data_json)
