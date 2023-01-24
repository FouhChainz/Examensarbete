import tkinter as tk
import sqlite3

# set colours
bg_colour="#3d6466"


def clear_widgets(frame):
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()


def fetch_db():
    # connect an sqlite database
    connection=sqlite3.connect("database/products.db")
    cursor=connection.cursor()

    # fetch all the table names
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables=cursor.fetchall()


    # fetch records from table
    table_name=all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records=cursor.fetchall()

    connection.close()

    return table_name, table_records


def pre_process(table_name, table_records):
    # preprocess table name
    title=table_name[:-6]
    title="".join([char if char.islower() else " " + char for char in title])

    # preprocess table records
    ingredients=[]

    for i in table_records:
        name=i[1]
        qty=i[2]
        unit=i[3]
        ingredients.append(qty + " " + unit + " of " + name)

    return title, ingredients


def load_frame1():
    clear_widgets(frame2)
    # stack frame 1 above frame 2
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    # create label widget for instructions
    tk.Label(
        frame1,
        text="Utrustning för sparande av vägd produkt",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
    ).pack()

    # create button widget
    tk.Button(
        frame1,
        text="Ny Sökning",
        bg="#28393a",
        command=lambda: load_frame2()
    ).pack(pady=20)

    tk.Button(
        frame1,
        text="Tidigare Sökningar",
        bg="#28393a",
        command=lambda: load_frame2()
    ).pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    # stack frame 2 above frame 1
    frame2.tkraise()

    # fetch from database
    table_name, table_records=fetch_db()
    title, ingredients=pre_process(table_name, table_records)


    # recipe title widget
    tk.Label(
        frame2,
        text=title,
        bg=bg_colour,
        fg="white",
        font=("Ubuntu", 20)
    ).pack(pady=25, padx=25)

    # recipe ingredients widgets
    for i in ingredients:
        tk.Label(
            frame2,
            text=i,
            bg="#28393a",
            fg="white",
            font=("Shanti", 12)
        ).pack(fill="both", padx=25)

    # 'back' button widget
    tk.Button(
        frame2,
        text="BACK",
        font=("Ubuntu", 18),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).pack(pady=20)


# initiallize app with basic settings
root=tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")


# create a frame widgets
frame1=tk.Frame(root, width=800, height=480, bg=bg_colour)
frame2=tk.Frame(root, bg=bg_colour)

# place frame widgets in window
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

# run app
root.mainloop()