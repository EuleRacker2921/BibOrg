import cv2
from pyzbar import pyzbar
from PIL import Image, ImageTk
import customtkinter
from tkinter import Label

class CameraFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.setup_sidebar()  # Diese Methode musst du entsprechend deinem Code definieren
        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.grid(row=1, column=5, sticky="nsew")  # Modified: Placed in column 2

        self.vid = cv2.VideoCapture(0)
        width, height = 800, 600
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.label = Label(self)
        self.label.grid(row=1, column=0, sticky="nsew")
        self.barcode_label = customtkinter.CTkLabel(self, text="Barcode:")
        self.barcode_label.grid(row=2, column=0, sticky="nsew")

        self.back_button = customtkinter.CTkButton(self, text="Zurück", command=self.master.go_back)
        self.back_button.grid(row=3, column=0, pady=10)

        self.open_camera()

    def setup_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Medium"  , command=lambda: self.master.switch_frame(self.master.new_media_frame))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde", command=lambda: self.master.switch_frame(self.master.new_customer_frame))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.favorite_button = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button.grid(row=3, column=0, padx=20, pady=10)
        self.favorite_button2 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button2.grid(row=4, column=0, padx=20, pady=10)
        self.favorite_button3 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button3.grid(row=5, column=0, padx=20, pady=10)
        self.favorite_button4 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button4.grid(row=6, column=0, padx=20, pady=10)
        self.favorite_button5 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button5.grid(row=8, column=0, padx=20, pady=10)
        self.favorite_button6 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button6.grid(row=9, column=0, padx=20, pady=10)
        self.favorite_button7 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button7.grid(row=10, column=0, padx=20, pady=10)
        self.favorite_button8 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button8.grid(row=11, column=0, padx=20, pady=10)
        self.favorite_button9 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button9.grid(row=12, column=0, padx=20, pady=10)
        self.favorite_button10 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button10.grid(row=13, column=0, padx=20, pady=10)
        self.favorite_button11 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button11.grid(row=14, column=0, padx=20, pady=10)
        self.favorite_button12 = customtkinter.CTkButton(self.sidebar_frame, text="", bg_color="transparent", fg_color="transparent", border_width=0, hover=False )
        self.favorite_button12.grid(row=15, column=0, padx=20, pady=10)




        self.go_back_button = customtkinter.CTkButton(self.sidebar_frame, text="Zurück", command=self.master.go_back)
        self.go_back_button.grid(row=16, column=0, padx=20, pady=10)
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.open_settings)	
        self.settings_button.grid(row=17, column=0, padx=20, pady=(10, 10))

    def open_camera(self):
        ret, frame = self.vid.read()
        if ret:
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                barcode_info = barcode.data.decode("utf-8")
                self.barcode_label.configure(text=f"Barcode: {barcode_info}")

            # Konvertiere das Bild für die Darstellung in Tkinter
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image)
            self.label.configure(image=photo_image)
            self.label.image = photo_image  # Referenz behalten, um Garbage Collection zu verhindern

        # Aktualisiere alle 10 Millisekunden
        self.label.after(10, self.open_camera)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def open_settings(self):
        self.master.switch_frame(self.master.settings_frame)