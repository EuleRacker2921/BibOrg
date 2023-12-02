import customtkinter


from .startView import StartFrame
from .loginView import LoginFrame
from .settingsView import settings_view_Frame
from .newBookView import NewBookFrame
from .newCustomerView import NewCustomerFrame


class App(customtkinter.CTk):
    def __init__(self, bibliothek, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bibliothek = bibliothek
        self.frame_stack = []
        self.current_frame = None

        self.start_frame = StartFrame
        self.settings_frame = settings_view_Frame
        self.new_book_frame = NewBookFrame
        self.new_customer_frame = NewCustomerFrame

        self.detail_view_media = None
        self.detail_view_media_type = None

        self.setup_app()
        self.switch_frame(LoginFrame)

    def setup_app(self):
        self.title("Bibliothek")
        self.geometry("720x480+0+0")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)        

    def switch_frame(self, frame_class, **kwargs):
        if self.current_frame is not None:
            self.current_frame.grid_forget()
            self.frame_stack.append(self.current_frame)
        self.current_frame = frame_class(self, **kwargs)  # Pass kwargs to frame_class
        self.current_frame.grid(row=0, column=0, sticky="nsew")


    def go_back(self):
        if self.frame_stack is not None:	
            self.current_frame.grid_forget()
            self.current_frame = self.frame_stack.pop()
            self.current_frame.grid(row=0, column=0, sticky="nsew")