import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time 
from tqdm import tqdm

API_KEY = "0d4995d3d47aec4a2cba0793bfd1f5f1"

with open("world_cities.txt","r", encoding="utf-8") as file:
    cities = [line.strip() for line in file.readlines()[:50]]
    
weather_data = [
    {
        "City": city,
        "Temperature (°C)": (data := requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0d4995d3d47aec4a2cba0793bfd1f5f1&units=metric"
        ).json()).get("main", {}).get("temp"),
        "Humidity (%)": data.get("main", {}).get("humidity"),
        "Weather": data.get("weather", [{}])[0].get("description")
    }
    for city in  tqdm(cities) if "main" in (time.sleep(1) or (data := requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0d4995d3d47aec4a2cba0793bfd1f5f1&units=metric"
    ).json()))
]

df = pd.DataFrame(weather_data).drop()
df.to_csv("world_weather.csv", index=False)

plt.figure(filesize=(12, 6))
sns.barplots(data=df, x="City", y="Temperature (°C)", hue="Weather", dodge=False)
plt.ticks(rotation=90)
plt.title("Temperature Across Cities")
plt.label("City")
plt.label("Temperature (°C)")
plt.legend(title="Weather Condition")
plt.show()