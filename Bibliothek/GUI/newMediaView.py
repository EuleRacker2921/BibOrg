import customtkinter

from ..datenmodelle.medien import Medien

class NewMediaFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.setup_sidebar()
        self.setup_widgets()

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


    def setup_widgets(self):
        self.bearbeiten_frame = customtkinter.CTkFrame(self, width=1000, height=800)
        self.bearbeiten_frame.grid(row=2, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.bearbeiten_frame.grid_rowconfigure(0, weight=1)
        self.bearbeiten_frame.grid_columnconfigure(0, weight=1)

        self.choose_item_type_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Medium auswählen", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.choose_item_type_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.bearbeiten_frame, dynamic_resizing=False,
                                                        values=["Buch", "Film", "Spiel"], command=self.optionmenu_callback)
        self.optionmenu_1.grid(row=1, column=0, padx=20, pady=(20, 10))

    def optionmenu_callback(self, value):
        self.optionmenu_1.grid_forget()
        self.bearbeiten_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Bearbeiten", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.bearbeiten_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.beabeiten_view_itemname = customtkinter.CTkLabel(self.bearbeiten_frame, text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_itemname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_item_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_item_entry.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")


        self.beabeiten_view_author = customtkinter.CTkLabel(self.bearbeiten_frame, text="Autor/Developer/Regisseur", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_author_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_author_entry.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_genre = customtkinter.CTkLabel(self.bearbeiten_frame, text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_genre_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_genre_entry.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_language = customtkinter.CTkLabel(self.bearbeiten_frame, text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_language_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_language_entry.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_year = customtkinter.CTkLabel(self.bearbeiten_frame, text="Erscheinungsjahr", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        self.beabeiten_view_year_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.beabeiten_view_year_entry.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

        self.beabeiten_view_description = customtkinter.CTkLabel(self.bearbeiten_frame, text="Beschreibung", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.beabeiten_view_description.grid(row=1, column=2,padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_description_entry = customtkinter.CTkTextbox(self.bearbeiten_frame, width=500, height=500)
        self.bearbeiten_view_description_entry.grid(row=2, column=2, columnspan=4,rowspan=4, padx=20, pady=(10, 10), sticky="w")


        if value == "Buch":
            self.create_book_view()
        elif value == "Film":
            self.create_movie_view()
        elif value == "Spiel":
            self.create_game_view()
        
        self.bearbeiten_button = customtkinter.CTkButton(self.bearbeiten_frame, text="Medium erstellen", command=self.create_new_media)
        self.bearbeiten_button.grid(row=9, column=1, padx=20, pady=(10, 10), sticky="w")

    def create_game_view(self):
        self.bearbeiten_platform_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Plattform", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_platform_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_platform_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_platform_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_multiplayer_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Multiplayer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_multiplayer_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_multiplayer_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_multiplayer_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_average_playtime_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Durchschnittliche Spielzeit", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_average_playtime_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_average_playtime_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_average_playtime_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")


    def create_movie_view(self):
        self.bearbeiten_duration_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Dauer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_duration_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_duration_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_duration_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_actors_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Schauspieler", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_actors_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_actors_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_actors_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_helpers_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Helfer", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_helpers_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_helpers_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_helpers_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")

    def create_book_view(self):
        self.bearbeiten_esbn_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="ESBN", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_esbn_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_isbn_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_isbn_entry.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_publisher_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_publisher_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_publisher_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_publisher_entry.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

        self.bearbeiten_pages_label = customtkinter.CTkLabel(self.bearbeiten_frame, text="Seiten", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.bearbeiten_pages_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
        self.bearbeiten_view_pages_entry = customtkinter.CTkEntry(self.bearbeiten_frame)
        self.bearbeiten_view_pages_entry.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w") 

    def create_new_media(self):
        media_data = [self.beabeiten_view_item_entry.get(), self.beabeiten_view_author_entry.get(), self.beabeiten_view_genre_entry.get(), self.beabeiten_view_year_entry.get(), self.bearbeiten_view_description_entry.get("1.0", "end-1c"), self.beabeiten_view_language_entry.get()]
        media_type = None
        print(media_data)
        if self.optionmenu_1.get() == "Buch":
            print("Buch")
            media_type = "book"
            media_data.append(self.bearbeiten_view_publisher_entry.get())
            media_data.append( self.bearbeiten_view_isbn_entry.get())
            media_data.append(self.bearbeiten_view_pages_entry.get())
        elif self.optionmenu_1.get() == "Film":
            print("Film")
            media_type = "film"
            media_data.append(self.bearbeiten_view_duration_entry.get())
            media_data.append(self.bearbeiten_view_actors_entry.get())
            media_data.append(self.bearbeiten_view_helpers_entry.get())
        elif self.optionmenu_1.get() == "Spiel":
            print("Spiel")
            media_type = "game"
            media_data.append(self.bearbeiten_view_platform_entry.get())
            media_data.append(self.bearbeiten_view_multiplayer_entry.get())
            media_data.append(self.bearbeiten_view_average_playtime_entry.get())
        self.master.bibliothek.add_media(media_data, item_type=media_type)
        self.master.switch_frame(self.master.start_frame)


    
    def open_settings(self):
        self.master.switch_frame(self.master.settings_frame)