import requests
import pandas as pd

# URL of the MTA API
api_url = "https://data.ny.gov/resource/vxuj-8kew.json"

# Fetching the data
response = requests.get(api_url)
data = response.json()

# Converting JSON data to DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('mta_data.csv', index=False)

print("Data fetched and saved to mta_data.csv")
