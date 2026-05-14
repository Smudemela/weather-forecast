import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"

params = {
	"latitude": 37.73,
	"longitude": -121.0,
	"hourly": ["temperature_2m", "precipitation", "windspeed_10m"],
	"past_days": 7,
	"forecast_days": 7
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])


print(df)