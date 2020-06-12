from tkinter import *
from tkinter import filedialog
import requests
import json

#import this to use normal images after . like .png etc 
#do: pip install Pillow
#sudo apt-get install python3-pil python3-pil.imagetk
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title('Weather App')
root.geometry("450x50")




try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=8B45E5B3-DACA-48C6-B6FC-36E275CE055E")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#00e400"
    elif category == "Moderate":
        weather_color = "#ffff00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff7e00"
    elif category == "Unhealthy":
        weather_color = "#ff0000"
    elif category == "Very Unhealthy":
        weather_color = "#8f3f97"
    elif category == "Hazardous":
        weather_color = "#7e0023"
  

    root.configure(background=weather_color)
    myLabel = Label(root, text=city + " " + "Air Quality " + str(quality) + " " + category, font=("Helvetiva", 20), background=weather_color)
    myLabel.pack()
except Exception as e:
    api = "Errorr.."





root.mainloop()


