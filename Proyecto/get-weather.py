import requests
import json
import csv
import os
import pathlib
from datetime import datetime

API_KEY = 'b794b9218f841b4d649bce12eacc5aed'
LAT = -0.2299
LON = -78.5249
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
OUTPUT_FILE = pathlib.Path(__file__).parent / 'clima-quito-hoy.csv'

def main():
    response = requests.get(URL)
    data = response.json()
    timestamp = datetime.now().isoformat()

    existe = os.path.isfile(OUTPUT_FILE)

    with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(['timestamp', 'data'])
        writer.writerow([timestamp, json.dumps(data)])

    print(f"[{timestamp}] Guardado - temp: {data['main']['temp']}°C")

if __name__ == '__main__':
    main()
