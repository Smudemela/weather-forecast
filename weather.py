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
df["hour"] = df["time"].dt.hour
df["day_of_year"] = df["time"].dt.day_of_year
df["temp_lag1"] = df["temperature_2m"].shift(1)
df["temp_rolling3"] = df["temperature_2m"].rolling(3).mean()
df = df.dropna()

print(df.head())
print(df.columns)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = df[["hour", "day_of_year", "temp_lag1", "temp_rolling3", "precipitation", "windspeed_10m"]]
y = df["temperature_2m"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor (n_estimator=100, random_state=42)