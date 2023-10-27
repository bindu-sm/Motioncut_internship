import tkinter as tk
import requests
import json

API_KEY = 'eb847b5fee75e5645562f51699723401'

def fetch_weather_data(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant weather information
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            
            temperature_label.config(text=f'Temperature: {temperature}°C')
            humidity_label.config(text=f'Humidity: {humidity}%')
            conditions_label.config(text=f'Conditions: {description}')
        else:
         
            result_label.config(text=f'Error: {data["message"]}')
    except requests.exceptions.RequestException as e:
        
        result_label.config(text='Network error. Check your connection.')


root = tk.Tk()
root.title('Weather App')


city_label = tk.Label(root, text='Enter city:')
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text='Fetch Weather', command=lambda: fetch_weather_data(city_entry.get()))
fetch_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

temperature_label = tk.Label(root, text='')
temperature_label.pack()

humidity_label = tk.Label(root, text='')
humidity_label.pack()

conditions_label = tk.Label(root, text='')
conditions_label.pack()


root.mainloop()
