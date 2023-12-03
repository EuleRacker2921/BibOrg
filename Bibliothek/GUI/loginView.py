import customtkinter

from ..datenbank import UsersDbhandler


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.setup_frame()
        self.setup_widgets()

    def setup_frame(self):
        self.place(relx=0.5, rely=0.5, anchor="center")


    def login(self, username, password, event=None):
        db = UsersDbhandler()
        user_validate = db.validate_user(username, password)
        if user_validate:
            self.master.geometry("1375x975")
            self.error_label.pack_forget()
            self.master.switch_frame(self.master.start_frame)
        else:
            self.error_label.configure(text="Benutzername oder Passwort falsch!")
            self.error_label.pack(pady=12, padx=10, anchor="s")
        

    def setup_widgets(self):
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20,padx=40,fill='both',expand=True) 

        label = customtkinter.CTkLabel(master=self.frame, text='Bibliothek Login')
        label.pack(pady=12, padx=10)

        user_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        user_entry.pack(pady=12, padx=10)

        user_pass = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        user_pass.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=self.frame, text='Login', command=lambda: self.login(user_entry.get(), user_pass.get()))
        button.pack(pady=12, padx=10)
        self.bind("<Return>", lambda event: self.login(user_entry.get(), user_pass.get()))

        self.error_label = customtkinter.CTkLabel(text="Falscher Benutzername oder Passwort", master=self, fg_color="red")