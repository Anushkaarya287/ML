import requests
import pandas as pd


url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()   
    print("Data received from API:\n", data)

    
    df = pd.DataFrame(data)
    print("\nConverted to DataFrame:\n", df)

    
    df.to_csv("api_users_data.csv", index=False)
    print("\nFile saved as api_users_data.csv")

else:
    print("Error:", response.status_code)