import pandas as pd
import os

# path to text file
txt_path = "iris.data.txt"

# column names for Iris dataset
columns = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm",
    "Species"
]

# read text file
df = pd.read_csv(txt_path, header=None, names=columns)

# save CSV ONE LEVEL UP (csv_project/)
csv_path = os.path.join("..", "Iris.csv")
df.to_csv(csv_path, index=False)

print("Iris.csv created successfully at:", csv_path)
