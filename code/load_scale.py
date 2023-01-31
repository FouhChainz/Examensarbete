import tkinter as tk
from tkinter import *
import load_search
from load_search import *


bg_color="#3d6466"

def init():
    testy.clear_widgets()
    # Stack Frame 3 over the others
    scale.tkraise()
    scale.pack_propagate(False)

# Todo
# Add Save button that saves to database
# Confirm popup with all data - Product - date/weight/weather. After confirm load_frame1()

# Create a Button to call close()
tk.Button(scale, text="Kill App", command=testy.close).grid(row=0, column=1, columnspan=5)

# Create a button to return to previous frame
tk.Button(scale, text="BACK", command=lambda: load_search.init()).grid(row=0, column=0)


def reWeigh ():
    serial_write()
    output=serial_read()
    vvalue.set(output)


tk.Button(scale,
          text="VÄG",
          command=lambda: reWeigh()
          ).grid(row=2, column=0)

vvalue=tk.StringVar(scale, value="Ställ din produkt på vågen och tryck på 'VÄG' ")
tk.Label(scale,
         textvariable=vvalue,
         height=5,
         width=50,
         font=("Arial", 15)
         ).grid(row=1, column=0, padx=20, pady=10)

tk.Label(scale,
         text=todays_date,
         height=5,
         width=20
         ).pack(padx=20, pady=20, side=LEFT)
tk.Label(scale,
         text=weather_temp,
         height=5,
         width=15
         ).pack(padx=20, side=LEFT)
tk.Label(scale,
         text=weather_status,
         height=5,
         width=15
         ).pack(padx=20, side=LEFT)
