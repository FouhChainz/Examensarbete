import tkinter as tk
from tkinter import *
import time
import serial
import datetime
import weather
from load_main import *


searchString= 'init value'
todays_date = datetime.date.today()
weather_status = weather.weather_description
weather_temp = weather.current_temperature

#Background color dark-green
bg_color="#3d6466"

#Initialize Serial Connection with USB-port
# ser=serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=None)

#Create function to send a signal to scale that it should weigh current object
def serial_write():
    ser.write(b's')

#Create function to read full line from scale and return it
def serial_read():
    x = ser.readline()
    return x

#Gör den ens något? Testa ta bort?
class SmartScale(tk.Tk):
    def __init__(self):
        super().__init__()

#Initiate and open connection to database


#Removes all widgets in all frames to prepare for next frame
def clear_widgets():
    for frame in (main, search, scale):
        #Select all frame widgets and delete them
        for widget in frame.winfo_children():
         widget.destroy()

#Kill application
def close():
   root.destroy()
   root.quit()

#Initialize app
root=tk.Tk()
#root.attributes('-fullscreen',True)  ---Commented out for testing phase.
root.title("Smart Scale")
root.geometry("800x480")

#root.resizable(False, False) -- Commented out for now

#Create a frame widget and places it in grid location
main=tk.Frame(root, width=800, height=480, bg=bg_color)
search=tk.Frame(root, width=800, height=480, bg=bg_color)
scale=tk.Frame(root, width=800, height=480, bg=bg_color)

#Sort grid in all frames
for frame in (main, search, scale):
    frame.grid(row=0, column=0, sticky="nesw")

#Load start page
load_main.init()
# Run app
root.mainloop()

