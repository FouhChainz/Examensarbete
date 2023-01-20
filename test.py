import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class ExampleApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x480")

        self.button = customtkinter.CTkButton(self,
                                         width=300,
                                         height=120,
                                         text="Ny Vägning",
                                         command=self.btn_search)
        self.button.place(relx=0.5, rely=0.1, anchor=tkinter.N)

        self.button2 = customtkinter.CTkButton(self,
                                         width=300,
                                         height=120,
                                         text="Tidigare Vägningar",
                                         command=self.btn_search)
        self.button2.place(relx=0.5, rely=0.6, anchor=tkinter.N)

        # self.button.pack(side="top", padx=40, pady=40)

    def create_searchbar(self):
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=0)

        self.textbox.insert("0.0", "Skriv in önskad produkt")  # insert at line 0 character 0
        self.text = self.textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

        self.textbox.configure(state="normal")  # configure textbox to be read-only

    def create_toplevel_search(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("700x380")
        self.create_searchbar()

    def btn_search(self):
        self.create_toplevel_search()

app = ExampleApp()
app.mainloop()