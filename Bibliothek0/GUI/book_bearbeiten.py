import tkinter
from typing import Optional, Tuple, Union
import customtkinter

from dbhandler import booksDbhandler

from new_book import NewBookFrame


class book_bearbeiten_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.book_id = self.master.detail_view_book
        self.book = self.get_book(self.book_id)

        self.setup_side_bar()
        self.setup_beabeiten_View()

    def setup_beabeiten_View(self):
        self.beabeiten_view = customtkinter.CTkFrame(self, width=1000, height=800 )
        self.beabeiten_view.grid(row=2, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.beabeiten_view.grid_rowconfigure(0, weight=1)
        self.beabeiten_view.grid_columnconfigure(0, weight=1)

        self.beabeiten_view_label = customtkinter.CTkLabel(self.beabeiten_view, text="Bearbeiten", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.beabeiten_view_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.beabeiten_view_bookname = customtkinter.CTkLabel(self.beabeiten_view, text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_bookname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_bookname_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_bookname_entry.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")
        self.beabeiten_view_bookname_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, value=self.book[1]))

        self.beabeiten_view_author = customtkinter.CTkLabel(self.beabeiten_view, text="Autor", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_author_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_author_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_author_entry, value=self.book[2]))
        self.beabeiten_view_author_entry.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_isbn = customtkinter.CTkLabel(self.beabeiten_view, text="ISBN", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_isbn.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_isbn_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_isbn_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[5]))
        self.beabeiten_view_isbn_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_genre = customtkinter.CTkLabel(self.beabeiten_view, text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_genre_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_genre_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[6]))
        self.beabeiten_view_genre_entry.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_language = customtkinter.CTkLabel(self.beabeiten_view, text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_language_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_language_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[7]))
        self.beabeiten_view_language_entry.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_publisher = customtkinter.CTkLabel(self.beabeiten_view, text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_publisher.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_publisher_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_publisher_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[8]))
        self.beabeiten_view_publisher_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")
        
        self.beabeiten_view_year = customtkinter.CTkLabel(self.beabeiten_view, text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_year_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_year_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[3]))
        self.beabeiten_view_year_entry.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_pages = customtkinter.CTkLabel(self.beabeiten_view, text="Seiten", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_pages.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_pages_entry = customtkinter.CTkEntry(self.beabeiten_view)
        self.beabeiten_view_pages_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.book[9]))
        self.beabeiten_view_pages_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_view_description = customtkinter.CTkLabel(self.beabeiten_view, text="Beschreibung", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_view_description.grid(row=2, column=2, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_description_entry = customtkinter.CTkTextbox(self.beabeiten_view)
        self.bearbeiten_view_description_entry.insert("0.0", text=self.book[4])
        self.bearbeiten_view_description_entry.grid(row=3, column=2, columnspan=5, rowspan=4, padx=20, pady=(10, 10), sticky="w")
        
        self.beabeiten_view_button = customtkinter.CTkButton(self.beabeiten_view, text="Speichern", command=self.bearbeite_save)
        self.beabeiten_view_button.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="w")

    def bearbeite_save(self):
        dbbooks = booksDbhandler()
        dbbooks.update_book(self.book_id,
                            self.beabeiten_view_bookname_entry.get(),
                            self.beabeiten_view_author_entry.get(),
                            self.beabeiten_view_year_entry.get(),
                            self.bearbeiten_view_description_entry.get("1.0", "end-1c"), 
                            self.beabeiten_view_isbn_entry.get(), 
                            self.beabeiten_view_genre_entry.get(),  
                            self.beabeiten_view_language_entry.get(),
                            self.beabeiten_view_publisher_entry.get(),
                            self.beabeiten_view_pages_entry.get())
        dbbooks.close()
        self.master.go_back()
        self.master.go_back()

    def setup_side_bar(self):
        
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch"  , command=lambda: self.master.switch_frame(NewBookFrame))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde", command=self.sidebar_button_event)
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
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.open_settings)	
        self.settings_button.grid(row=17, column=0, padx=20, pady=(10, 10))

    def open_settings(self):
        pass

    def sidebar_button_event(self):
        pass

    def get_book(self, book_id):
        dbbooks = booksDbhandler()
        book = dbbooks.get_book(book_id)
        return book

    def back_button_event(self):
        self.master.go_back()