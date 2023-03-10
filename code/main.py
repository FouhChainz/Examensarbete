import tkinter as tk
from tkinter import *
import time
import serial
import datetime
import weather
import mysql.connector
from mysql.connector import Error

searchString='init value'

todays_date=datetime.date.today()
weather_status=weather.weather_description
weather_temp=weather.current_temperature
date_string = todays_date.strftime('%Y-%m-%d')

flagga=0
product_weight=0
product_name = "testy"

# Background color dark-green
bg_color="#3d6466"


# Initialize Serial Connection with USB-port
# ser=serial.Serial(
#     port='/dev/ttyUSB0',
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=None)

# Create function to send a signal to scale that it should weigh current object
def serial_write ():
    ser.write(b's')


# Create function to read full line from scale and return it
def serial_read ():
    x=ser.readline()
    return x


def insert_into_database (product=product_name,
                          vikt=product_weight,
                          datum=todays_date,
                          temperature=weather_temp,
                          weather_status=weather_status):
    print(product)
    print(vikt)
    print(datum)
    print(temperature)
    print(weather_status)
    try:
        connection=mysql.connector.connect(host='localhost',
                                           database='products',
                                           user='user0',
                                           password='')
        cursor=connection.cursor()

        name=product_name

        mySql_insert_query="""CREATE TABLE IF NOT EXISTS """ + name + """( 
	                                Datum DATE NOT NULL,
	                                Vikt DOUBLE(4,2) NOT NULL,
	                                PRIMARY KEY(Datum)
                                    );"""
        mySql_insert_query2="""
                                INSERT INTO """ + name + """(Datum, Vikt) 
                                   VALUES (%s, %s); """
        mySql_insert_query3="""
                                INSERT INTO V??der(Datum, Temperatur, V??der_Status)
                                    VALUES (%s,%s,%s);"""

        value= product
        value2=(product, date_string,vikt)
        value3=(date_string ,temperature,weather_status)
        cursor.execute(mySql_insert_query,)
        cursor.execute(mySql_insert_query2,value2)
        cursor.execute(mySql_insert_query3,value3)

        connection.commit()
        print("Record inserted successfully into %s table", product)

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Removes all widgets in all frames to prepare for next frame
def clear_widgets ():
    for frame in (main, search, scale):
        # Select all frame widgets and delete them
        for widget in frame.winfo_children():
            widget.destroy()


# Kill application
def close ():
    root.destroy()
    root.quit()


def ny_s??kning ():
    global flagga
    flagga=1
    load_search()


def se_statistik ():
    global flagga
    flagga=0
    load_search()


# Load main(start) page
def load_main ():
    clear_widgets()
    # Stack Main frame above other frames
    main.tkraise()
    # Prevent widgets from modifying the frame
    main.pack_propagate(False)

    # Create label widget for instructions
    tk.Label(
        main,
        text="Utrustning f??r sparande av v??gd produkt",
        bg=bg_color,
        fg="white",
    ).pack(pady=25)

    # Create button widget
    tk.Button(
        main,
        text="Ny V??gning",
        width=50,
        height=10,
        bg="#28393a",
        command=lambda:ny_s??kning()
    ).pack(pady=20)

    # Create a Button to call close()
    tk.Button(main, text="Kill App", command=close).grid(row=0, column=1, columnspan=5)

    tk.Button(
        main,
        text="Se lagrad data",
        width=50,
        height=10,
        bg="#28393a",
        command=lambda:se_statistik()
    ).pack(pady=20)


def load_search (searchString=searchString):
    clear_widgets()
    # Stack Search frame above other frames
    search.tkraise()
    main.pack_propagate(False)

    # Title text
    tk.Label(
        search,
        text="S??k efter ??nskad produkt",
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
        command=lambda:load_main()
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
        # Loads next page depending on what you pressed on the main page
        elif value == 'Enter':
            global product_name
            product_name=load_search.searchString
            print("product name: " + product_name)
            print("Search string: " + load_search.searchString)
            if flagga:
                load_scale()
            elif not flagga:
                load_stats()
        # Remove last pressed letter
        elif value == '???':
            i=textArea.get(1.0, END)
            j=i[ :-2 ]
            textArea.delete(1.0, END)
            textArea.insert(INSERT, j)
        # Change to CAPITAL LETTERS
        elif value == 'Caps':
            capsButtons=[ 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '??', '???',
                          'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '??', '??', 'Enter',
                          '', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-',
                          'Space' ]

            varRow=2
            varColumn=1

            for button in capsButtons:
                command=lambda x=button:select(x)
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

            buttons=[ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '??', '???',
                      'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '??', '??', 'Enter',
                      '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
                      'Space' ]

            for button in buttons:
                command=lambda x=button:select(x)
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

    varRow=2
    varColumn=1

    buttons=[ 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '??', '???',
              'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '??', '??', 'Enter',
              '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
              'Space' ]

    for button in buttons:
        command=lambda x=button:select(x)
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


# Load frame where you weigh products
def load_scale ():
    clear_widgets()
    # Stack Frame 3 over the others
    scale.tkraise()
    scale.pack_propagate(False)

    # Todo
    # Add Save button that saves to database
    # Confirm popup with all data - Product - date/weight/weather. After confirm load_frame1()

    # Create a Button to call close()
    tk.Button(scale, text="Kill App", command=close).grid(row=0, column=1, columnspan=5)

    # Create a button to return to previous frame
    tk.Button(scale, text="BACK", command=lambda:load_search()).grid(row=0, column=0)

    def reWeigh ():
        insert_into_database()
        serial_write()
        output=serial_read()
        global product_weight
        product_weight=output
        vvalue.set(output)

    tk.Button(scale,
              text="V??G",
              command=lambda:reWeigh()
              ).grid(row=2, column=0)

    vvalue=tk.StringVar(scale, value="St??ll din produkt p?? v??gen och tryck p?? 'V??G' ")
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


def load_stats ():
    clear_widgets()
    # Stack Frame 3 over the others
    stats.tkraise()
    stats.pack_propagate(False)

    tk.Label(stats,
             text='hej',
             height=5,
             width=15
             ).pack(padx=20, side=LEFT)


# Initialize app
root=tk.Tk()
# root.attributes('-fullscreen',True)  ---Commented out for testing phase.
root.title("Smart Scale")
root.geometry("800x480")

# root.resizable(False, False) -- Commented out for now

# Create a frame widget and places it in grid location
main=tk.Frame(root, width=800, height=480, bg=bg_color)
search=tk.Frame(root, width=800, height=480, bg=bg_color)
scale=tk.Frame(root, width=800, height=480, bg=bg_color)
stats=tk.Frame(root, width=800, height=480, bg=bg_color)

# Sort grid in all frames
for frame in (main, search, scale, stats):
    frame.grid(row=0, column=0, sticky="nesw")

# Load start page
load_main()
# Run app
root.mainloop()
