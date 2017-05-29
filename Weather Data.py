import tkinter as tk
import time
import json
import requests
from PIL import Image, ImageTk
from pprint import pprint





class Home:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Today's Weather")

        # Colors
        header_text_color = "white"
        header_bg_color = "sky blue"

        body_bg_color = "white"
        body_text_color = "black"

        # Fonts
        standard_font = ("Helvetica", 15)

        # Initialize frames
        self.header = tk.Frame(bg=header_bg_color)
        self.body = tk.Frame(bg=body_bg_color)

        # Header
        self.set_location()

        tk.Label(self.header, text=self.city, font=("Helvetica", 30), fg=header_text_color, bg=header_bg_color).grid(row=0, column=0)

        date = time.strftime("%A %x")
        tk.Label(self.header, text=date, font=standard_font, fg=header_text_color, bg=header_bg_color).grid(row=0, column=2)

        time_ = time.strftime("%H:%M")
        tk.Label(self.header, text=time_, font=standard_font, fg=header_text_color, bg=header_bg_color).grid(row=1, column=2)

        icon = ImageTk.PhotoImage(Image.open("weather icon small.png"))
        self.icon_label = tk.Label(self.header, text="", image=icon, bg=header_bg_color)
        self.icon_label.image = icon
        self.icon_label.grid(row=2, column=1)

        # Body
        self.set_weather_data()

        temp = self.weather_data["main"]["temp"] * (9.0/5.0) - 459.67           # Convert from Kelvin to Farenheight
        tk.Label(self.body, text=str(temp)[:4], font=standard_font, fg=body_text_color, bg=body_bg_color).grid(row=0, column=0)


        # Grid frames to root
        self.header.grid(row=0)
        self.body.grid(row=1)



    def set_location(self):
        url = 'http://ipinfo.io/json'
        response = requests.get(url)
        data = json.loads(response.text)

        IP = data['ip']
        org = data['org']
        self.city = data['city']
        self.country = data['country']
        self.region = data['region']

    def set_weather_data(self):
        api_key = "59af29e891e63c457d4bd56217c66e36"
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}".format(self.city, api_key))
        pprint(r.json())
        self.weather_data = r.json()
        self.weather_icon = requests.get("http://openweathermap.org/img/w/{0}.png".format(self.weather_data["weather"]["icon"]))

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()







def main():
    home = Home()

    home.start()






if __name__ == "__main__":
    main()