import customtkinter
import tkinter as tk
from StartSite import StartSiteFrame

from dbhandler import usersDbhandler
import tkinter.messagebox as messagebox


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1) 
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        

        self.user_name = customtkinter.CTkEntry(placeholder_text="Benutzername", master=self)
        self.user_name.grid(row=1, column=1, pady=12, padx=10, sticky="nsew")
        
        self.user_pass = customtkinter.CTkEntry(placeholder_text="Password", show="*", master=self)
        self.user_pass.grid(row=2, column=1, pady=12, padx=10, sticky="nsew") 

        button = customtkinter.CTkButton(text='Login',command=lambda: self.login(self.user_name.get(), self.user_pass.get()), master=self, width=200, height=100 )
        button.grid(row=3, column=1, rowspan=2, pady=12, padx=10) 

        self.error_label = customtkinter.CTkLabel(text="Falscher Benutzername oder Passwort", master=self, fg_color="red")
    
    def login(self, username, password): 
        db = usersDbhandler()
        
        user_validate = db.validate_user(username, password)
        if user_validate:
            self.master.switch_frame(StartSiteFrame)
            print("Login successful")
            self.master.geometry("1375x975")  # Set the frame size to 1080x720

        # Rest of the code...
        
            return True
        else:
            print("Login failed. Please check your username and password.")
            #messagebox.showinfo("ERROR", "Login failed. Please check your username and password.")
            self.error_label.grid(row=5, column=1, pady=12, padx=10, sticky="nsew")
            return False
        
    def logout(self):
        pass