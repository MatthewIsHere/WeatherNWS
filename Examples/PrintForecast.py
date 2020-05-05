"""This Example Will Print The Forecast To The Console"""
from weatherapi import forecast
import time

while True:
    forecast = forecast("aiken", "sc")
    print(forecast.CountyName)
    print(forecast.forecast[0].detailedForecast)
