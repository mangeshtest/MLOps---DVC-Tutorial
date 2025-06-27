import pandas as pd
import os

data = {
    "name": ["Raj", "Om", "Rohan"],
    "marks": [90, 89, 98],
    "grade": ["A", "B", "A+"]
}

df = pd.DataFrame(data)

new_row1 = {"name": "Neha", "marks": 85, "grade": "B+"}
df.loc[len(df)] = new_row1

new_row2 = {"name": "Rohit", "marks": 94, "grade": "A"}
df.loc[len(df)] = new_row2

folder_name = "data"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"Data file saved to: {file_path}")