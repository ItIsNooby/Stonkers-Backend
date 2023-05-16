from flask import FLask, jsonify
import requests

# Set your RapidAPI project and API key
project_name = 'YOUR_RAPIDAPI_PROJECT_NAME'
api_key = 'YOUR_RAPIDAPI_API_KEY'

# Set the API endpoint and parameters
endpoint = 'getRealtimeStockPrices'
params = {
    'symbol': 'AAPL'  # Replace with the desired stock symbol
}

# Make the API call
headers = {
    'X-RapidAPI-Host': 'nasdaq-realtime-stock-pricing.p.rapidapi.com',
    'X-RapidAPI-Key': api_key
}

response = requests.get(
    f'https://nasdaq-realtime-stock-pricing.p.rapidapi.com/{endpoint}',
    params=params,
    headers=headers
)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print('Response:', data)
else:
    print('Error:', response.status_code)