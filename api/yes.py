import requests

url = "https://nasdaq-stock-pricing.p.rapidapi.com/Stock/GetPrice/AAPL"

headers = {
	"X-RapidAPI-Key": "b731fee7a5mshf2b6608334c0b07p13bf5fjsn09fcf5df26f4",
	"X-RapidAPI-Host": "nasdaq-stock-pricing.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())