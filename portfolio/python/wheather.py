import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import seaborn as sns
import key
import os
import csv

sns.set(style="darkgrid")

#API_key=key.key
API_key="7c83fe38eaa3d158fae999677be6ce32"
CITY="Gwalior"
Units="metric"

time_data=[]
temp_data=[]
feels_like_data=[]
humidity_data=[]
wind_speed_data=[]

fig, ax=plt.subplots()

csv_file="weather_log.csv"
file_exists=os.path.isfile(csv_file)

if not file_exists:
    with open(csv_file,mode='w',
    newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Time","Temperature (C)","Humidity (%)","Wind_Speed (w/s)"])

def get_weather_data():
    url=f"https://api.openweathermap.org/data/2.5/weather?q=(CITY)&appid=7c83fe38eaa3d158fae999677be6ce32&units=metric"
    response=requests.get(url).json()

    temp=response["main"]["temp"]
    humidity=response["main"]["humidity"]
    wind_speed=response["main"]["speed"]

    return temp,humidity,wind_speed

def update():
    now=datetime.now().strftime
    ("%H:%M:%S")
    temp,humidi                                                                                                                        