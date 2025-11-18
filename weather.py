import requests

# Quotes API endpoint
url = "https://api.quotable.io/random"

response = requests.get(url)

if response.status_code == 200:
    quote = response.json()
    print("Quote:", quote["content"])
    print("Author:", quote["author"])
else:
    print("Error:", response.status_code)
