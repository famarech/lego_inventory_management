import pandas as pd
csv_data = pd.read_csv("sets.txt", sep = "\t")
csv_data.to_json("sets.json", orient = "records")