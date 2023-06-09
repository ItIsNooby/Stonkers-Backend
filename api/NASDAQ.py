from flask import Flask, jsonify
import requests

# Set your RapidAPI project and API key
project_name = 'Nasdaq Stock Pricing'
api_key = 'b731fee7a5mshf2b6608334c0b07p13bf5fjsn09fcf5df26f4'

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
    f'https://nasdaq-realtime-stock-pricing.p.rapidapi.com//Stock/GetPrice/AAPL',
    params=params,
    headers=headers
)

# Handle the response
if response.status_code == 200:
    data = response.json()
    print('Response:', data)
else:
    print('Error:', response.status_code)