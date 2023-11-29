import customtkinter
import tkinter as tk

from dbhandler import booksDbhandler


class NewBookFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = customtkinter.CTkLabel(text="Hi", master=self)
        self.label.grid(row=1)


        


