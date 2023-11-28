import settings
import dbhandler
import tkinter
import customtkinter

class Bibliothek(customtkinter.CTk):
    def __init__(self, title, geometry, resizable):
        self.title = title
        self.geometry = geometry
        self.resizable = resizable
        
    def start_app(self):
        self.root.mainloop()
    