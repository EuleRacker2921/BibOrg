import customtkinter

class NewBookFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.setup_frame()
        self.setup_widgets()

    def setup_frame(self):
        pass

    def setup_widgets(self):
        pass
    