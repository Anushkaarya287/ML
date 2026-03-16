import pandas as pd
import os

txt_path = "iris.data.txt"

columns = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm",
    "Species"
]


df = pd.read_csv(txt_path, header=None, names=columns)


csv_path = os.path.join("..", "Iris.csv")
df.to_csv(csv_path, index=False)

print("Iris.csv created successfully at:", csv_path)
