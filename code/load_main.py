import tkinter as tk
from tkinter import *
import load_search



#Background color dark-green
bg_color="#3d6466"
main=tk.Frame(testy.main, width=800, height=480, bg=bg_color)


def init():
    clear_widgets()
    # Stack Main frame above other frames
    testy.main.tkraise()
    # Prevent widgets from modifying the frame
    testy.main.pack_propagate(False)

# Create label widget for instructions
tk.Label(
    main,
    text="Utrustning för sparande av vägd produkt",
    bg=bg_color,
    fg="white",
).pack(pady=25)

# Create button widget
tk.Button(
    main,
    text="Ny Vägning",
    width=50,
    height=10,
    bg="#28393a",
    command=lambda:load_search.init()
).pack(pady=20)

# Create a Button to call close()
tk.Button(main, text="Kill App", command=close).grid(row=0, column=1, columnspan=5)

tk.Button(
    main,
    text="Se lagrad data",
    width=50,
    height=10,
    bg="#28393a",
    command=lambda:load_search.init()
).pack(pady=20)
