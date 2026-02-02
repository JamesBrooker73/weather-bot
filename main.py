import tkinter as tk
from openweathermap import OpenWeatherMap


def fetch_weather():
  print("fetching weather!")
  owm = OpenWeatherMap("London")
  owm.fetchWeather()

def main():

  root = tk.Tk()
  root.title("WeatherBot!")

  locationLabel = tk.Label(root, text="Location")
  searchButton = tk.Button(root, text="Search", width=10, command=fetch_weather)


  locationLabel.grid(row=0, column=0)
  searchButton.grid(row=0, column=1)

  root.mainloop()

if __name__ == "__main__":
    main()

