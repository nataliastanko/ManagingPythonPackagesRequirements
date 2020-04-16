import requests

# Euro foreign exchange reference rates
response = requests.get("https://api.exchangeratesapi.io/latest?symbols=CAD,GBP,PLN")
print(response.text)
