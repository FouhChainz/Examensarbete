import tkinter as tk
from tkinter import *


class createKeyboard():

    def __init__(self, value):
        self.value = value

    createKeyboard=Tk()
    createKeyboard.title("On Screen Keyboard")
    createKeyboard.resizable(False, False)

    titleLabel=tk.Label(createKeyboard,
                        text="On Screen Keyboard",
                        font=('arial', 20, 'bold'))
    titleLabel.grid(row=0, column=0, columnspan=15)

    textArea=tk.Text(createKeyboard,
                     font=('arial', 20, 'bold'),
                     height=10,
                     width=100)
    textArea.grid(row=1, column=0, columnspan=15)

    def command(self,value):
        createKeyboard.select(value)

    def select(self,value, textArea=textArea):
        if value == 'Space':
            textArea.insert(INSERT, ' ')

        # elif value=='Enter':

        elif value == '←':
            i=textArea.get(1.0, END)
            j=i[:-2]
            textArea.delete(1.0, END)
            textArea.insert(INSERT, j)

        elif value == 'Caps':
            capsButtons=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←',
                         'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'Å',
                         'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', 'Enter',
                         'Shift ⇧', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '-', '⇧ Shift',
                         'Space']

            varRow=2
            varColumn=1

            for button in capsButtons:
                createKeyboard.command(self,button)
                if button != 'Enter' and button != 'Space':
                    tk.Button(createKeyboard, text=button, width=5, height=2, command=self.command).grid(row=varRow,
                                                                                                    column=varColumn)
                if button == 'Space':
                    tk.Button(createKeyboard, text=button, width=50, command=self.command).grid(row=6, column=0,
                                                                                           columnspan=15)
                if button == 'Enter':
                    tk.Button(createKeyboard, text=button, width=8, height=2, command=self.command).grid(row=3, column=13)

                varColumn+=1
                if varRow == 2 and varColumn > 11:
                    varColumn=1
                    varRow+=1
                elif varRow == 3 and varColumn > 11:
                    varColumn=0
                    varRow+=1
                elif varRow == 4 and varColumn > 12:
                    varColumn=0
                    varRow+=1
                elif varRow == 5 and varColumn > 13:
                    varColumn=0
                    varRow+=1

        elif value == 'CAPS':

            varRow=2
            varColumn=1

            buttons=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←',
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å',
                     'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
                     'Shift ⇧', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-', '⇧ Shift',
                     'Space']

            for button in buttons:
                createKeyboard.command(self,button)
                if button != 'Enter' and button != 'Space':
                    tk.Button(createKeyboard, text=button, width=5, height=2, command=self.command(button)).grid(row=varRow, column=varColumn)
                if button == 'Space':
                    tk.Button(createKeyboard, text=button, width=50, command=self.command(button)).grid(row=6, column=0,columnspan=15)
                if button == 'Enter':
                    tk.Button(createKeyboard, text=button, width=8, height=2, command=self.command(button)).grid(row=3, column=13)

                varColumn+=1
                if varRow == 2 and varColumn > 11:
                    varColumn=1
                    varRow+=1
                elif varRow == 3 and varColumn > 11:
                    varColumn=0
                    varRow+=1
                elif varRow == 4 and varColumn > 12:
                    varColumn=0
                    varRow+=1
                elif varRow == 5 and varColumn > 13:
                    varColumn=0
                    varRow+=1

        else:
         textArea.insert(INSERT, value)

    varRow=2
    varColumn=1

    buttons=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←',
             'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'å',
             'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä', 'Enter',
             'Shift ⇧', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-', '⇧ Shift',
             'Space']

    for button in buttons:
        createKeyboard.command(button)
        if button != 'Enter' and button != 'Space':
            tk.Button(createKeyboard, text=button, width=5, height=2, command=command).grid(row=varRow,column=varColumn)
        if button == 'Space':
            tk.Button(createKeyboard, text=button, width=50, command=command).grid(row=6, column=0, columnspan=15)
        if button == 'Enter':
            tk.Button(createKeyboard, text=button, width=8, height=2, command=command).grid(row=3, column=13)

        varColumn+=1
        if varRow == 2 and varColumn > 11:
            varColumn=1
            varRow+=1
        elif varRow == 3 and varColumn > 11:
            varColumn=0
            varRow+=1
        elif varRow == 4 and varColumn > 12:
            varColumn=0
            varRow+=1
        elif varRow == 5 and varColumn > 13:
            varColumn=0
            varRow+=1

    createKeyboard.mainloop()
