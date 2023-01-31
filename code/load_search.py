import tkinter as tk
from tkinter import *
import load_main
import load_scale

searchString= 'init value'
bg_color="#3d6466"
search=tk.Frame(root, width=800, height=480, bg=bg_color)



def init(searchString=searchString):
    clear_widgets()
    # Stack Search frame above other frames
    search.tkraise()
    main.pack_propagate(False)

# Title text
tk.Label(
    search,
    text="Sök efter önskad produkt",
    bg=bg_color,
    fg="white",
    font=("Ubuntu", 20)
).grid(row=0, column=1, columnspan=15)

# 'back' button widget
tk.Button(
    search,
    text="BACK",
    font=("Ubuntu", 18),
    bg="#28393a",
    fg="black",
    command=lambda: load_main.init()
).grid(row=0, column=0)

# Create a Button to call close()
tk.Button(search, text="Kill App", command=close).grid(row=0, column=1, columnspan=5)

# Load textbox that shows input
textArea=tk.Text(search,
                 height=5,
                 width=50
                 )
textArea.grid(row=1, column=2, columnspan=15)


# Function that controls logic behind button presses
def select (value, textArea=textArea, searchString=searchString):
    # Add blankspace
    if value == 'Space':
        textArea.insert(INSERT, ' ')
    # Loads next page
    elif value == 'Enter':
        load_scale.init()
    # Remove last pressed letter
    elif value == '←':
        i=textArea.get(1.0, END)
        j=i[ :-2 ]
        textArea.delete(1.0, END)
        textArea.insert(INSERT, j)
    # Change to CAPITAL LETTERS
    elif value == 'Caps':
        capsButtons=[ 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Å', '←',
                      'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', 'Enter',
                      '', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-',
                      'Space' ]

        varRow=2
        varColumn=1

        for button in capsButtons:
            command=lambda x=button: select(x)
            if button != 'Enter' and button != 'Space' and button != '':
                tk.Button(search, text=button, width=2, height=5, command=command).grid(row=varRow,
                                                                                        column=varColumn)
            if button == 'Space':
                tk.Button(search, text=button, width=50, height=4, command=command).grid(row=5, column=1,
                                                                                         columnspan=25)
            if button == 'Enter':
                tk.Button(search, text=button, width=3, height=6, command=command).grid(row=3, column=12)
            if button == '':
                tk.Button(search)

            varColumn+=1
            if varRow == 2 and varColumn > 12:
                varColumn=0
                varRow+=1
            elif varRow == 3 and varColumn > 12:
                varColumn=1
                varRow+=1
            elif varRow == 4 and varColumn > 11:
                varColumn=1
                varRow+=1

    # Change from CAPITAL LETTERS to Small
    elif value == 'CAPS':
        varRow=2
        varColumn=1

        buttons=[ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '←',
                  'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
                  '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
                  'Space' ]

        for button in buttons:
            command=lambda x=button: select(x)
            if button != 'Enter' and button != 'Space' and button != '':
                tk.Button(search, text=button, width=2, height=5, command=command).grid(row=varRow,
                                                                                        column=varColumn)
            if button == 'Space':
                tk.Button(search, text=button, width=50, height=4, command=command).grid(row=5, column=1,
                                                                                         columnspan=25)
            if button == 'Enter':
                tk.Button(search, text=button, width=3, height=6, command=command).grid(row=3, column=12)
            if button == '':
                tk.Button(search)

            varColumn+=1
            if varRow == 2 and varColumn > 12:
                varColumn=0
                varRow+=1
            elif varRow == 3 and varColumn > 12:
                varColumn=1
                varRow+=1
            elif varRow == 4 and varColumn > 11:
                varColumn=1
                varRow+=1

    # Save pressed button to search string
    else:
        textArea.insert(INSERT, value)
        load_search.searchString=textArea.get(1.0, END)
        print(load_search.searchString)  # For testing purposes REMOVE LATER ON


varRow=2
varColumn=1

buttons=[ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '←',
          'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
          '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
          'Space' ]

for button in buttons:
    command=lambda x=button: select(x)
    if button != 'Enter' and button != 'Space' and button != '':
        tk.Button(search, text=button, width=2, height=5, command=command).grid(row=varRow, column=varColumn)
    if button == 'Space':
        tk.Button(search, text=button, width=50, height=4, command=command).grid(row=5, column=1, columnspan=25)
    if button == 'Enter':
        tk.Button(search, text=button, width=3, height=6, command=command).grid(row=3, column=12)
    if button == '':
        tk.Button(search)

    varColumn+=1
    if varRow == 2 and varColumn > 12:
        varColumn=0
        varRow+=1
    elif varRow == 3 and varColumn > 12:
        varColumn=1
        varRow+=1
    elif varRow == 4 and varColumn > 11:
        varColumn=1
        varRow+=1
