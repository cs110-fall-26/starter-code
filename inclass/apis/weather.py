import requests
from sys import argv
import json

API_TOKEN="YOUR API TOKEN GOES HERE"

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={API_TOKEN}"
    return requests.get(url).json()

def get_forecast(location):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&APPID={API_TOKEN}"
    return requests.get(url).json()

def k_to_f(kelvin):
    return (9/5) * (kelvin - 273.15)  + 32


def format_raw(data):
    return json.dumps(data, indent=1)

def format_date(forecast_date):
    format = ""
    # TODO Take the data of an individual forecast date and format it into a readable form and not just a JSON format
    return format


def format_forecast(forecast_data):
    format = ""
    # TODO Take the data received from the forecast and format it so it's easier to view.
    return format

def main():
    if (len(argv) < 3):
        print(f"Invalid usage: python3 {argv[0]} <location> <current, forecast> <raw=default / clean>")
        return
    location = argv[1]
    data_type = argv[2]
    output_type = "raw"
    if len(argv) == 4:
        output_type = argv[3]

    if data_type == "current":
        if output_type == "raw":
            print(format_raw(get_weather(location)))
        elif output_type == "clean":
            print(format_date(get_weather(location)))
    elif data_type == "forecast":
        if output_type == "raw":
            print(format_raw(get_forecast(location)))
        elif output_type == "clean":
            print(format_forecast(get_forecast(location)))
    else:
        print("Invalid type, defaulting to current weather")
        print(format_date(get_weather(location)))

if __name__ == "__main__":
    main()


