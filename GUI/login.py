import customtkinter
import tkinter as tk
from StartSite import StartSiteFrame

from dbhandler import usersDbhandler


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.user_name = customtkinter.CTkEntry(placeholder_text="Benutzername", master=self)
        self.user_name.grid(row=0, column=0, pady=12, padx=10)
        
        self.user_pass = customtkinter.CTkEntry(placeholder_text="Password", show="*", master=self)
        self.user_pass.grid(row=1, column=0, pady=12, padx=10) 

        button = customtkinter.CTkButton(text='Login',command=lambda: self.login(self.user_name.get(), self.user_pass.get()), master=self )
        button.grid(row=2, column=0, pady=12, padx=10) 

        checkbox = customtkinter.CTkCheckBox(text='Remember Me', master=self) 
        checkbox.grid(row=3, column=0, pady=12, padx=10) 

    def login(self, username, password): 
        db = usersDbhandler()
        
        user_validate = db.validate_user(username, password)
        if user_validate:
            self.master.switch_frame(StartSiteFrame)
            print("Login successful")
            return True
        return False
    
    def logout(self):
        pass