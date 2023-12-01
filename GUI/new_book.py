import customtkinter
import tkinter as tk
from new_customer import NewCustomerFrame
from dbhandler import booksDbhandler


class NewBookFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.setup_side_bar()
        self.setup_form_new_book()


    def setup_side_bar(self):
        
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch"  , text_color_disabled="red", fg_color="white")
        self.sidebar_button_1.configure(state="disabled")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde" , text_color_disabled="red", fg_color="white")
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




        self.go_back_button = customtkinter.CTkButton(self.sidebar_frame, text="Zurück", command=self.master.go_back)
        self.go_back_button.grid(row=16, column=0, padx=20, pady=10)
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.open_settings)	
        self.settings_button.grid(row=17, column=0, padx=20, pady=(10, 10))


    
    def setup_form_new_book(self):
        self.new_book_frame = customtkinter.CTkFrame(self, width=800, height=800, corner_radius=10)
        self.new_book_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.new_book_frame.grid_rowconfigure(10, weight=1)
                
        self.book_label = customtkinter.CTkLabel(self.new_book_frame, text="Neues Buch", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.book_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.bool_name_label = customtkinter.CTkLabel(self.new_book_frame, text="Titel")
        self.bool_name_label.grid(row=2, column=0, padx=20, pady=(10, 0))        
        self.book_name = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Titel")
        self.book_name.grid(row=2, column=1, pady=12, padx=10, sticky="nsew")

        self.book_author_label = customtkinter.CTkLabel(self.new_book_frame, text="Autor")
        self.book_author_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        self.book_author = customtkinter.CTkEntry(self.new_book_frame,placeholder_text="Autor")
        self.book_author.grid(row=3, column=1, pady=12, padx=10, sticky="nsew")


        self.book_isbn_label = customtkinter.CTkLabel(self.new_book_frame, text="ISBN")
        self.book_isbn_label.grid(row=2, column=2, padx=20, pady=(10, 0))
        self.book_isbn = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="ISBN")
        self.book_isbn.grid(row=2, column=3, pady=12, padx=10, sticky="nsew")

        self.book_genre_label = customtkinter.CTkLabel(self.new_book_frame, text="Genre")
        self.book_genre_label.grid(row=3, column=2, padx=20, pady=(10, 0))
        self.book_genre = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Genre")
        self.book_genre.grid(row=3, column=3, pady=12, padx=10, sticky="nsew")

        self.book_language_label = customtkinter.CTkLabel(self.new_book_frame, text="Sprache")
        self.book_language_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        self.book_language = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Sprache")
        self.book_language.grid(row=4, column=1, pady=12, padx=10, sticky="nsew")

        self.book_pages_label = customtkinter.CTkLabel(self.new_book_frame, text="Seiten")  
        self.book_pages_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.book_pages = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Seiten")
        self.book_pages.grid(row=5, column=1, pady=12, padx=10, sticky="nsew")

        self.book_publisher_label = customtkinter.CTkLabel(self.new_book_frame, text="Verlag")
        self.book_publisher_label.grid(row=4, column=2, padx=20, pady=(10, 0))
        self.book_publisher = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Verlag")
        self.book_publisher.grid(row=4, column=3, pady=12, padx=10, sticky="nsew")

        self.book_year_label = customtkinter.CTkLabel(self.new_book_frame, text="Jahr")
        self.book_year_label.grid(row=5, column=2, padx=20, pady=(10, 0))
        self.book_year = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Jahr")
        self.book_year.grid(row=5, column=3, pady=12, padx=10, sticky="nsew")

        self.book_description_label = customtkinter.CTkLabel(self.new_book_frame, text="Beschreibung")
        self.book_description_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.book_description = customtkinter.CTkEntry(self.new_book_frame, placeholder_text="Beschreibung")
        self.book_description.grid(row=10, column=1, columnspan=2, pady=12, padx=10, sticky="nsew")

        button = customtkinter.CTkButton(self.new_book_frame, text='Buch hinzufügen',command=self.create_new_book, width=200, height=100 )
        button.grid(row=11, column=1, rowspan=2, pady=12, padx=10)

    def open_settings(self):
        pass

    def back_button_event(self):
        self.master.go_back()

    def create_new_book(self):
        dbbook = booksDbhandler()
        dbbook.add_book(self.book_name.get(), self.book_author.get(), self.book_isbn.get(), self.book_genre.get(), self.book_language.get(), self.book_pages.get(), self.book_publisher.get(), self.book_year.get(), self.book_description.get(), False)
        self.master.go_back()

        


