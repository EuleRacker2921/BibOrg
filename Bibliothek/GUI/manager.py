import customtkinter

from ..datenmodelle.bibliothek import Bibliothek


from .startView import StartFrame, ItemFrame
from .loginView import LoginFrame
from .settingsView import settings_view_Frame
from .newMediaView import NewMediaFrame
from .newCustomerView import NewCustomerFrame
from .mediaEditView import EditMediaFrame
from .detailsView import DetailsFrame
from .cameraView import CameraFrame

class App(customtkinter.CTk):
    def __init__(self, bibliothek, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bibliothek = bibliothek
        self.frame_stack = []
        self.current_frame = None

        self.start_frame = StartFrame
        self.settings_frame = settings_view_Frame
        self.new_media_frame = NewMediaFrame
        self.new_customer_frame = NewCustomerFrame
        self.edit_media_frame = EditMediaFrame
        self.detail_view_frame = DetailsFrame
        self.login_frame = LoginFrame
        self.item_frame = ItemFrame
        self.camera_frame = CameraFrame

        self.detail_view_media = None
        self.detail_view_media_type = None

        self.setup_app()
        self.switch_frame(self.login_frame)

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