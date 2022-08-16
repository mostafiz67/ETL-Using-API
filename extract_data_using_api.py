# Import the required modules and functions
import requests
import pandas as pd

# Extract Data Using ExchangeRate-API
# Call the API
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=raWK4v77bkpWTXKtsnNnSQw5SFUbHe1P" 
response = requests.get(url)
response.json()

# Save as DataFrame

# Turn the data into a dataframe
dataframe = pd.DataFrame(response.json())
dataframe

# Drop unnescessary columns
dataframe.drop(columns=["success", "timestamp", "base", "date"], inplace=True)
dataframe

# Load as CSV File
dataframe.to_csv("exchange_rates_1.csv")
