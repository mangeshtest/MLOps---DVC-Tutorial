import pandas as pd
import os

data = {
    "name": ["Raj", "Om", "Rohan"],
    "marks": [90, 89, 98],
    "grade": ["A", "B", "A+"]
}

df = pd.DataFrame(data)

folder_name = "data"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"Data file saved to: {file_path}")