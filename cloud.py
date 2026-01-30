import pandas as pd

# Simulated cloud download (local file)
print("Downloading file from cloud storage...")

df = pd.read_csv("api_users_data.csv")
print(df.head())
