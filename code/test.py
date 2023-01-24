import tkinter as tk
from tkinter import *
import sqlite3

bg_color="#3d6466"
searchString = 'init value'


class Kiosk(tk.Tk):
    def __init__(self):
        super().__init__()


def fetch_db():
    connection=sqlite3.connect("products.db")
    c=connection.cursor()



    connection.commit()
    connection.close()


def clear_widgets(frame):
    #Select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()


def load_main():
    clear_widgets(search)
    clear_widgets(scale)
    #Stack Main Frame above other frames
    main.tkraise()
    #Prevent widgets from modifying the frame
    main.pack_propagate(False)

    #Create label widget for instructions
    tk.Label(
        main,
        text="Utrustning för sparande av vägd produkt",
        bg=bg_color,
        fg="white",
    ).pack(pady=25)

    #Create button widget
    tk.Button(
        main,
        text="Ny Sökning",
        width=50,
        height=10,
        bg="#28393a",
        command=lambda: load_search()
    ).pack(pady=20)

    tk.Button(
        main,
        text="Tidigare Sökningar",
        width=50,
        height=10,
        bg="#28393a",
        command=lambda: load_search()
    ).pack(pady=20)

    tk.Button(
        main,
        text="Lägg in ny Produkt- ToDo?",
        width=50,
        height=10,
        bg="#28393a"
        # , command=lambda: load_search()
    ).pack(pady=20)


def load_search(searchString=searchString):
    clear_widgets(main)
    clear_widgets(scale)
    #Stack Search Frame above other frames
    search.tkraise()
    main.pack_propagate(False)

    #Fetch from database
    fetch_db()

    # Title widget to help
    tk.Label(
        search,
        text="Sök efter önskad produkt",
        bg=bg_color,
        fg="white",
        font=("Ubuntu", 20)
    ).grid(row=0, column=1, columnspan=15)

    #'back' button widget
    tk.Button(
        search,
        text="BACK",
        font=("Ubuntu", 18),
        bg="#28393a",
        fg="black",
        command=lambda: load_main()
    ).grid(row=0, column=0)

    #Load area where you can see the letters pressed
    textArea=tk.Text(search,
                     height=5,
                     width=50
                     )
    textArea.grid(row=1, column=2,columnspan=15)

    #Function that controls logic behind button presses
    def select(value, textArea=textArea,searchString=searchString):
        #Add blankspace
        if value == 'Space':
            textArea.insert(INSERT, ' ')
        #Loads next page
        elif value=='Enter':
            load_frame3()
        #Remove last pressed letter
        elif value == '←':
            i=textArea.get(1.0, END)
            j=i[:-2]
            textArea.delete(1.0, END)
            textArea.insert(INSERT, j)
        #Change to CAPITAL LETTERS
        elif value == 'Caps':
            capsButtons=['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Å', '←',
                         'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', 'Enter',
                         '', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-',
                         'Space']

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

        #Change from CAPITAL LETTERS to Small
        elif value == 'CAPS':
            varRow=2
            varColumn=1

            buttons=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '←',
                     'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
                     '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
                     'Space']

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

        #Save pressed button to search string
        else:
            textArea.insert(INSERT, value)
            load_search.searchString = textArea.get(1.0, END)
            print(load_search.searchString)
    varRow=2
    varColumn=1

    buttons=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '←',
             'Caps','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
             '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
             'Space']

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

#Load new frame
def load_frame3():
    clear_widgets(search)
    clear_widgets(main)
    #Stack Frame 3 over the others
    scale.tkraise()
    scale.pack_propagate(False)

    # Todo
    # Add live output from scale
    # Add Save button that saves to database
    # Confirm popup with all data - Product - date/weight/weather. After confirm load_frame1()


    print('Value searched: ' + load_search.searchString)

# Initialize app
root=tk.Tk()
root.title("Smart Scale")
root.geometry("800x480")
# root.resizable(False, False)

# Create a frame widget and places it in grid location
main=tk.Frame(root, width=800, height=480, bg=bg_color)
search=tk.Frame(root, width=800, height=480, bg=bg_color)
scale=tk.Frame(root, width=800, height=480, bg=bg_color)

# Sort grid in all frames
for frame in (main, search, scale):
    frame.grid(row=0, column=0, sticky="nesw")

# Load start page
load_main()

# Run app
root.mainloop()

