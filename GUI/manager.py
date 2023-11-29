import tkinter
import customtkinter

from login import LoginFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = LoginFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    
    


if __name__ == "__main__":
    app = App()
    app.mainloop()