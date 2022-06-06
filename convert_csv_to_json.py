import pandas as pd
csv_data = pd.read_csv("Parts.csv", sep = "\t")
csv_data.to_json("parts.json", orient = "records")