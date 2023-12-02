import tkinter
import customtkinter

from login import LoginFrame

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_stack = []
        self.current_frame = None
        self.setup_app()
        
        
        self.detail_view_book = None

        self._frame = None

        self.switch_frame(LoginFrame)   

    def setup_app(self):
        self.title("Bücherei")
        self.geometry("720x480+0+0")  # Set window size and position
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)


    def switch_frame(self, frame_class, **kwargs):
        if self.current_frame is not None:
            self.current_frame.grid_forget()
            self.frame_stack.append(self.current_frame)
        self.current_frame = frame_class(self, **kwargs)  # Pass kwargs to frame_class
        self.current_frame.grid(row=0, column=0, sticky="nsew")


    def go_back(self):
        if self.frame_stack:
            self.current_frame.grid_forget()
            self.current_frame = self.frame_stack.pop()
            self.current_frame.grid(row=0, column=0, sticky="nsew")
    
    def setup_app(self):
        self.title("Bücherei")
        self.geometry("720x480")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    app.mainloop()