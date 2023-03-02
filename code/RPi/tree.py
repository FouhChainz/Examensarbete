from tkinter import *
from tkinter import ttk
import pandas as pd
root = Tk()
root.title("titel")
root.geometry("500x500")

my_tree = ttk.Treeview(root)


my_tree['columns'] = ("Name", "ID", "Favourite Pizza")

my_tree.column("#0", width=0)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favourite Pizza",anchor=W,width=120)

my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Favourite Pizza",anchor=W)

my_tree.insert(parent='',index='end', iid=0, text="", values=("John",1,"Pepperoni"))

my_tree.pack(pady=20)

root.mainloop()


####################


tk.Label(stats,
         text="Datum",
         bg=bg_color,
         fg='black',
         font=('Arial', 30, 'bold', 'underline')
         ).grid(row=0, column=0, padx=20, pady=20)
tk.Label(stats,
         text="Vikt(g)",
         bg=bg_color,
         fg='black',
         font=('Arial', 30, 'bold', 'underline')
         ).grid(row=0, column=1, padx=20, pady=20)
for i in range(total_rows):
    tk.Label(stats,
             text=read_from_db[ i ][ 0 ],
             bg=bg_color,
             fg='black',
             font=('Arial', 15)
             ).grid(row=i + 1, column=0, padx=20)
    tk.Label(stats,
             text=read_from_db[ i ][ 1 ],
             bg=bg_color,
             fg='black',
             font=('Arial', 15)
             ).grid(row=i + 1, column=1, padx=20)