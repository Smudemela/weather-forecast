# Weather Forecast - Folsom, CA

A machine learning project that fetches real-time weather data and predicts hourly temperatures using a Random Forest model.

## What it does
- Fetches live weather data from the Open-Meteo API
- Engineers features like lag temperatures and rolling averages
- Trains a Random Forest ML model to predict temperatures
- Visualizes actual vs predicted temperatures on a chart

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Open-Meteo API

## How to run

1. Clone the repo
   git clone https://github.com/Smudemela/weather-forecast.git

2. Create and activate virtual environment
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install requests pandas scikit-learn matplotlib

4. Run the project
   python3 weather.py

## Results
The model achieves a Mean Absolute Error (MAE) of ~1.2°F which means predictions are on average only 1.2 degrees off from the actual temperature.

## Project Milestones
- Set up a Python project from scratch
- Learned Git & GitHub
- Fetched live data from a real API
- Cleaned and prepared data with Pandas
- Built and trained a real ML model
- Achieved ~1.2°F prediction accuracy
- Created a professional chart
- Wrote a professional README
- Pushed everything to GitHub

*Last Updated May 22*
