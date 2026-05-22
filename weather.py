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

# time             - the date and hour of the reading
# temperature_2m   - the actual temperature in Fahrenheit
# ...              - pandas hides middle columns (precipitation, windspeed, hour, day_of_year)
# temp_lag1        - the previous hour's temperature
# temp_rolling3    - the average of the last 3 hours temperatures

df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])  # date and hour of the reading
df["hour"] = df["time"].dt.hour  # hour of the day (0-23)
df["day_of_year"] = df["time"].dt.day_of_year  # day of the year (1-365)
df["temperature_2m"] = (df["temperature_2m"] * 9/5) + 32  # temp converted to fahrenheit
df["temp_lag1"] = df["temperature_2m"].shift(1)  # previous hour's temperature
df["temp_rolling3"] = df["temperature_2m"].rolling(3).mean()  # average of last 3 hours
df = df.dropna()  # remove rows with missing values

print(df.head())
print(df.columns)

# ── ML Model ──
# learns patterns from data to predict temperature

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = df[["hour", "day_of_year", "temp_lag1", "temp_rolling3", "precipitation", "windspeed_10m"]]
y = df["temperature_2m"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

model = RandomForestRegressor (n_estimators=100, random_state=42)

model.fit(X_train, y_train) #fit means "study this data".handing the model the training data (X_train = the clues, y_train = the answers) and it goes through all of it to figure out the patterns between them.

predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error
print("MAE", mean_absolute_error(y_test, predictions))

import matplotlib.pyplot as plt
plt.plot(df["time"], df["temperature_2m"], label="Actual")
sorted_idx = y_test.index.sort_values()
plt.plot(df["time"].iloc[sorted_idx], predictions[sorted_idx.argsort()], label="Predicted")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.title("Actual vs Predicted Temperature - Folsom, CA")
plt.show()


