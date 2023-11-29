import tkinter
import customtkinter

from login import LoginFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.setup_app()

        self._frame = None

        self.switch_frame(LoginFrame)   

        self.my_frame = LoginFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    def setup_app(self):
        self.geometry("1080x720")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    app.mainloop()