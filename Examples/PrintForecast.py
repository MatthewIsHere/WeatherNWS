"""This Example Will Print The Forecast To The Console"""
from WeatherNWS import API
import time
api = API("Test User") #PUT IDENTIFICATION HERE
while True:
    forecast = api.forecast("aiken", "sc")
    print(forecast["county"])
    print(forecast["forecast"][0]["detailedForecast"])
    time.sleep(60)
