import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("test")
        self.geometry("800x480")
        tabview = customtkinter.CTkTabview(self, width=800, height=390)
        tabview.pack()

        tabview.add("Hem")  # Hemskärm
        tabview.add("Sök")  # Skärm där man söker efter produkt
        tabview.add("Väg")  # Skärmen där man väger produkt och sparar värde
        tabview.add("Ny Produkt")  # Lägger till ny produkt i databasen
        tabview.set("Hem")  # set currently visible tab

        def btn_search():
            tabview.set("Sök")
        def btn_new_input():
            tabview.set("Sök")

        button = customtkinter.CTkButton(tabview.tab("Hem"), text="Ny vägning", command=btn_search, width=125, height=50)
        button.pack(padx=20, pady=20)
        button = customtkinter.CTkButton(tabview.tab("Hem"), text="Tidigare vägningar", command=btn_search, width=100, height=50)
        button.pack(padx=20, pady=20)
        button = customtkinter.CTkButton(tabview.tab("Hem"), text="Lägg in ny produkt", command=btn_new_input, width=100, height=50)
        button.pack(padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()