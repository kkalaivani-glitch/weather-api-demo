import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap key
city = "Warangal"         # Change to any city (e.g., Hyderabad)

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code, response.text)
