import tkinter as tk
import time
import json
import requests
from PIL import Image, ImageTk





class Home:
    def __init__(self):
        self.root = tk.Tk()

        text_color = "white"
        bg_color = "sky blue"

        self.root.title("Today's Weather")
        self.root.config(bg=bg_color)

        self.set_location()

        tk.Label(text=self.city, font=("Helvetica", 30), fg=text_color, bg=bg_color).grid(row=0, column=0)

        date = time.strftime("%A %x")
        tk.Label(text=date, font=("Helvetica", 15), fg=text_color, bg=bg_color).grid(row=0, column=2)

        time_ = time.strftime("%H:%M")
        tk.Label(text=time_, font=("Helvetica", 15), fg=text_color, bg=bg_color).grid(row=1, column=2)

        icon = ImageTk.PhotoImage(Image.open("weather icon.png"))
        tk.Label(text="", image=icon).grid(row=2, column=1)

    def set_location(self):
        url = 'http://ipinfo.io/json'
        response = requests.get(url)
        data = json.loads(response.text)

        IP = data['ip']
        org = data['org']
        self.city = data['city']
        self.country = data['country']
        self.region = data['region']

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()







def main():
    home = Home()

    home.start()






if __name__ == "__main__":
    main()