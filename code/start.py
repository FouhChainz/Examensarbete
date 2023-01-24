import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x400")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app,
                                 width=300,
                                 height=120,
                                 text="Ny Vägning",
                                 command=button_function)
button.place(relx=0.5, rely=0.1, anchor=tkinter.N)


button = customtkinter.CTkButton(master=app,
                                 width=300,
                                 height=120,
                                 text="Tidigare Vägningar",
                                 command=button_function)
button.place(relx=0.5, rely=0.6, anchor=tkinter.N)

app.mainloop()
