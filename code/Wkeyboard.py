import tkinter as tk
from tkinter import *
bg_color="#3d6466"



root=Tk()
root.configure(background=bg_color)
root.geometry("800x480")
root.title("On Screen Keyboard")
root.resizable(False, False)

textArea=tk.Text(root,
                    font=('arial', 20, 'bold'),
                    height=5,
                    width=50
                    )
textArea.grid(row=0, column=0, columnspan=15)

def select(value, textArea=textArea):
    if value == 'Space':
        textArea.insert(INSERT, ' ')

        # elif value=='Enter':

    elif value == '←':
        i=textArea.get(1.0, END)
        j=i[:-2]
        textArea.delete(1.0, END)
        textArea.insert(INSERT, j)

    elif value == 'Caps':
        capsButtons=[ 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Å','←',
                    'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', 'Enter',
                    '','Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-',
                    'Space']

        varRow=1
        varColumn=1

        for button in capsButtons:
            command = lambda x=button: select(x)
            if button != 'Enter' and button != 'Space' and button != '':
                tk.Button(root, text=button, width=3, height=5, command=command).grid(row=varRow, column=varColumn)
            if button == 'Space':
                tk.Button(root, text=button, width=50, height=2, command=command).grid(row=5, column=0, columnspan=15)
            if button == 'Enter':
                tk.Button(root, text=button, width=1, height=6, command=command).grid(row=2, column=13)
            if button == '':
                tk.Button(root)

            varColumn+=1
            if varRow == 1 and varColumn > 12:
                varColumn=1
                varRow+=1
            elif varRow == 2 and varColumn > 12:
                varColumn=0
                varRow+=1
            elif varRow == 3 and varColumn > 11:
                varColumn=0
                varRow+=1


    elif value == 'CAPS':
        varRow=1
        varColumn=1

        buttons=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å', '←',
                 'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
                 '', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
                 'Space']

        for button in buttons:
            command=lambda x=button: select(x)
            if button != 'Enter' and button != 'Space' and button != '':
                tk.Button(root, text=button, width=3, height=5, command=command).grid(row=varRow, column=varColumn)
            if button == 'Space':
                tk.Button(root, text=button, width=50, height=2, command=command).grid(row=5, column=0, columnspan=15)
            if button == 'Enter':
                tk.Button(root, text=button, width=1, height=6, command=command).grid(row=2, column=13)
            if button == '':
                tk.Button(root)

            varColumn+=1
            if varRow == 1 and varColumn > 12:
                varColumn=1
                varRow+=1
            elif varRow == 2 and varColumn > 12:
                varColumn=0
                varRow+=1
            elif varRow == 3 and varColumn > 11:
                varColumn=0
                varRow+=1


    else:
     textArea.insert(INSERT, value)

varRow=1
varColumn=1


buttons=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å','←',
             'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
              '','z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-',
             'Space']

for button in buttons:
    command=lambda x=button: select(x)
    if button != 'Enter' and button != 'Space' and button != '':
        tk.Button(root, text=button, width=3, height=5, command=command).grid(row=varRow,column=varColumn)
    if button == 'Space':
        tk.Button(root, text=button, width=50,height=2 , command=command).grid(row=5, column=0, columnspan=15)
    if button == 'Enter':
        tk.Button(root, text=button, width=1, height=6, command=command).grid(row=2, column=13)
    if button == '':
        tk.Button(root)

    varColumn+=1
    if varRow == 1 and varColumn > 12:
        varColumn=1
        varRow+=1
    elif varRow == 2 and varColumn > 12:
        varColumn=0
        varRow+=1
    elif varRow == 3 and varColumn > 11:
        varColumn=0
        varRow+=1

root.mainloop()
