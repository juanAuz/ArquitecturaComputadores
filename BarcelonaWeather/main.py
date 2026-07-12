import pandas as pd
import requests
import os
import pathlib
import json
import csv


BarcelonaLat = 41.38879
BarcelonaLon = 2.15899
API_KEY = "b794b9218f841b4d649bce12eacc5aed"
fileName = pathlib.Path(__file__).parent / 'clima-barcelona-hoy.csv'


def getWeather(lat, lon, api):
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric"
    response = requests.get(URL)
    return response.json()


def write2csv(json_processed, csvFile):
    if os.path.isfile(csvFile):
        antiguo = pd.read_csv(csvFile)
        df=pd.concat([antiguo, json_processed], ignore_index=True)
    else:
        df = json_processed
    df.to_csv(csvFile, index=False)

def process(data):
    if "weather" in data and isinstance(data["weather"], list) and data["weather"]:
        data["weather_description"] = data["weather"][0].get("description", None)
        del data["weather"]
    else:
        data["weather_description"] = None
    return pd.json_normalize(data, sep="_")

def main():
    Barcelona_weather = getWeather(lat=BarcelonaLat, lon=BarcelonaLon, api=API_KEY)
    if Barcelona_weather['cod']!=404:
        jsonProcesado=process(Barcelona_weather)
        write2csv(jsonProcesado,fileName)
    else:
        print("Ciudad no disponible o API KEY no válida")
if __name__ == '__main__':
    main()
