import tkinter
import customtkinter
from dbhandler import customerDbhandler

from settings import settings_view_Frame


class NewCustomerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.setup_side_bar()   
        self.setup_form_new_customer()
    
    def back_button_event(self):

        self.master.go_back()

    def setup_form_new_customer(self):
        
        self.frame_new_customer = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.frame_new_customer.place(relx=0.5, rely=0.5, anchor="center")
        self.frame_new_customer.grid_rowconfigure(10, weight=1)
        # Logo
        self.new_customer_label = customtkinter.CTkLabel(self.frame_new_customer, text="Neuer Kunde", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_customer_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.new_customer_name = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Name")
        self.new_customer_name.grid(row=1, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_adresse = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Adresse")
        self.new_customer_adresse.grid(row=3, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_phone = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Telefonnummer")
        self.new_customer_phone.grid(row=4, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_email = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Email")
        self.new_customer_email.grid(row=5, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_username = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Benutzername")
        self.new_customer_username.grid(row=6, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_password = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Passwort")
        self.new_customer_password.grid(row=7, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_age = customtkinter.CTkEntry(self.frame_new_customer, placeholder_text="Alter")
        self.new_customer_age.grid(row=2, column=0, pady=12, padx=10, sticky="nsew")

        self.new_customer_button = customtkinter.CTkButton(self.frame_new_customer, text="Kunde erstellen", command=self.create_new_customer)
        self.new_customer_button.grid(row=8, column=0, pady=12, padx=10, sticky="nsew")
        
        
    def create_new_customer(self):
        dbcustomer = customerDbhandler()
        dbcustomer.add_customer(self.new_customer_name.get(), self.new_customer_adresse.get(), self.new_customer_phone.get(), self.new_customer_email.get(), self.new_customer_username.get(), self.new_customer_password.get(), self.new_customer_age.get())
        self.master.go_back()

    def setup_side_bar(self):



        
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch")
        self.sidebar_button_1.configure(state="disabled")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde")
        self.sidebar_button_2.configure(state="disabled")
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




        self.go_back_button = customtkinter.CTkButton(self.sidebar_frame, text="Zurück", command=self.back_button_event)
        self.go_back_button.grid(row=16, column=0, padx=20, pady=10)
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=lambda: self.master.switch_frame(settings_view_Frame))	
        self.settings_button.grid(row=17, column=0, padx=20, pady=(10, 10))


        