from typing import Optional, Tuple, Union
import customtkinter
from ..datenmodelle import medien

import tkinter

class EditMediaFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, item,  **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.item:medien.Medien = item

        self.setup_side_bar()
        self.setup_widget()

    def setup_side_bar(self):
        
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




        self.go_back_button = customtkinter.CTkButton(self.sidebar_frame, text="Zurück", command=lambda: self.master.go_back())
        self.go_back_button.grid(row=16, column=0, padx=20, pady=10)
        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=lambda: self.master.switch_frame(self.master.settings_frame))
        self.settings_button.grid(row=17, column=0, padx=20, pady=(10, 10))

    def setup_widget(self):
        self.bearbeiten_frame = customtkinter.CTkFrame(self, width=1000, height=800)
        self.bearbeiten_frame.grid(row=2, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.bearbeiten_frame.grid_rowconfigure(0, weight=1)
        self.bearbeiten_frame.grid_columnconfigure(0, weight=1)


        self.bearbeiten_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Bearbeiten", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bearbeiten_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.beabeiten_view_itemname = customtkinter.CTkLabel(self.bearbeiten_frame, text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_itemname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_item_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_item_entry.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")
        self.beabeiten_view_item_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_item_entry, value=self.item.titel)) 

        self.beabeiten_view_author = customtkinter.CTkLabel(self.bearbeiten_frame, text="Autor/Developer/Regisseur", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_author_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_author_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_author_entry, value=self.item.autor_oder_regisseur))
        self.beabeiten_view_author_entry.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_genre = customtkinter.CTkLabel(self.bearbeiten_frame, text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_genre_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_genre_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_genre_entry, self.item.genre))
        self.beabeiten_view_genre_entry.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_language = customtkinter.CTkLabel(self.bearbeiten_frame, text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_language_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_language_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_language_entry, self.item.language))
        self.beabeiten_view_language_entry.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_year = customtkinter.CTkLabel(self.bearbeiten_frame, text="Erscheinungsjahr", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_year_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_year_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_year_entry, self.item.publication_year))
        self.beabeiten_view_year_entry.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")
        if type(self.item) == medien.Buch:
            print("Buch")
            self.setup_book_edit()
        elif type(self.item) == medien.Film:
            print("Film")
            self.setup_film_edit()
        elif type(self.item) == medien.Spiel:
            print("Spiel")
            self.setup_game_edit()

        self.bearbeiten_view_description = customtkinter.CTkLabel(self.bearbeiten_frame, text="Beschreibung", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_view_description.grid(row=2, column=2, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_description_entry = customtkinter.CTkTextbox(self.bearbeiten_frame)
        self.bearbeiten_view_description_entry.insert("1.0",str(self.item.description))
        self.bearbeiten_view_description_entry.grid(row=3, column=2, columnspan=5, rowspan=4, padx=20, pady=(10, 10), sticky="w")
        
        self.beabeiten_view_button = customtkinter.CTkButton(self.bearbeiten_frame, text="Speichern", command=self.bearbeiten_save)
        self.beabeiten_view_button.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="w")

    
    def setup_book_edit(self):
        self.bearbeiten_esbn_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="ESBN", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_esbn_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_isbn_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_isbn_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_isbn_entry, self.item.ESBN))
        self.bearbeiten_view_isbn_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_publisher_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_publisher_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_publisher_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_publisher_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_publisher_entry, self.item.publisher))
        self.bearbeiten_view_publisher_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_pages_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Seiten", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_pages_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_pages_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_pages_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_pages_entry, self.item.pages))
        self.bearbeiten_view_pages_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w") 

    def setup_film_edit(self):
        self.bearbeiten_duration_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Dauer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_duration_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_duration_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_duration_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_duration_entry, self.item.duration))
        self.bearbeiten_view_duration_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_actors_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Schauspieler", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_actors_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_actors_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_actors_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_actors_entry, self.item.actors))
        self.bearbeiten_view_actors_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_helpers_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Helfer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_helpers_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_helpers_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_helpers_entry.configure(textvariable=tkinter.StringVar(self.bearbeiten_view_helpers_entry, self.item.helpers))
        self.bearbeiten_view_helpers_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")

    def setup_game_edit(self):
        self.bearbeiten_platform_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Plattform", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_platform_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_platform_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_platform_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.item.platform))
        self.bearbeiten_view_platform_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_multiplayer_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Multiplayer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_multiplayer_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_multiplayer_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_multiplayer_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.item.multiplayer))
        self.bearbeiten_view_multiplayer_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_average_playtime_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Durchschnittliche Spielzeit", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_average_playtime_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_average_playtime_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_average_playtime_entry.configure(textvariable=tkinter.StringVar(self.beabeiten_view_bookname_entry, self.item.average_playtime))
        self.bearbeiten_view_average_playtime_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")



    def bearbeiten_save(self):
        self.item.titel = self.beabeiten_view_item_entry.get()
        self.item.autor_oder_regisseur = self.beabeiten_view_author_entry.get()
        self.item.genre = self.beabeiten_view_genre_entry.get()
        self.item.publication_year = self.beabeiten_view_year_entry.get()
        self.item.description = self.bearbeiten_view_description_entry.get("0.0", "end")
        self.item.language = self.beabeiten_view_language_entry.get()
        
        if type(self.item) == medien.Buch:
            media_type = "book"
            self.item.publisher = self.bearbeiten_view_publisher_entry.get()
            self.item.pages = self.bearbeiten_view_pages_entry.get()
            self.item.ESBN = self.bearbeiten_view_isbn_entry.get()
        elif type(self.item) == medien.Film:
            media_type = "film"
            self.item.duration = self.beabeiten_view_duration_entry.get()
            self.item.actors = self.bearbeiten_view_actors_entry.get()
            self.item.helpers = self.bearbeiten_view_helpers_entry.get()
        elif type(self.item) == medien.Spiel:
            media_type = "game"
            self.item.platform = self.bearbeiten_view_platform_entry.get()
            self.item.multiplayer = self.bearbeiten_view_multiplayer_entry.get()
            self.item.average_playtime = self.bearbeiten_view_average_playtime_entry.get()

        self.master.bibliothek.update_media(self.item, item_type=media_type)
        self.master.switch_frame(self.master.start_frame)
