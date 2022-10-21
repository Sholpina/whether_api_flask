import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# API_KEY = open('api_key', 'r').read()
API_KEY = "63cd7f0721c48e12c646259601dcf911"
CITY = "Baku"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
# print(response)

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
fells_like_kelvin = response['main']['feels_like']
fells_like_celsius, fells_like_fahrenheit = kelvin_to_celsius_fahrenheit(fells_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f} C or {temp_fahrenheit:.2f}F")
print(f'Temperature in {CITY} feels like: {fells_like_celsius:.2f} C or {fells_like_fahrenheit:.2f} F')
print(f"Humidity in {CITY}: {humidity} %")
print(f"Wind speed in {CITY}: {description} local time.")
print(f"General weather in {CITY}: {humidity} %")
print(f"Sun rises in {CITY}: at {sunrise_time} local time")
print(f"Sun sets in {CITY}:at {sunset_time} local time")

print(sunrise_time)
print(sunset_time)
