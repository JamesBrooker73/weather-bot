import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

class OpenWeatherMap():
  def __init__(self, location):
    self.location = location

  def fetchWeather(self):
    cityName = "Nottingham"
    #url = f'http://api.openweathermap.org/geo/1.0/direct?q={cityName}&appid={API_KEY}'
    url = f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_KEY}'
    response = requests.get(url)
    print(response.json())