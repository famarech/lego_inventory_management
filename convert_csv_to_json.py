import pandas as pd
csv_data = pd.read_csv("Parts.csv", sep = "\t", encoding="utf-8")
csv_data.to_json("parts.json", orient = "records")