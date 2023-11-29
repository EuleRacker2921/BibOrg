import customtkinter


from new_book import NewBookFrame
from dbhandler import booksDbhandler


class StartSiteFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch"  , command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Test", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Search Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(10, 10), sticky="nsew")

        def search_book():
            booksdb = booksDbhandler()
            search_text = self.entry.get()  # Get the text entered in the CTkEntry widget
            selected_book = booksdb.search_for_book(search_text)
            self.overview_tab_bookname_info.configure(text=selected_book[0][1])
            self.overview_tab_author_info.configure(text=selected_book[0][2])
            self.overview_tab_isbn_info.configure(text=selected_book[0][5])
            self.overview_tab_genre_info.configure(text=selected_book[0][6])
            self.overview_tab_language_info.configure(text=selected_book[0][7])
            self.overview_tab_publisher_info.configure(text=selected_book[0][8])
            self.overview_tab_year_info.configure(text=selected_book[0][3])

            print(selected_book[0][1])

        # Search Button
        self.search_button = customtkinter.CTkButton(self, text="Search", command=search_book)
        self.search_button.grid(row=0, column=3, padx=(0, 20), pady=(20, 20), sticky="nsew")
        # Camera Scan Button
        self.camera_scan_button = customtkinter.CTkButton(self, text="Scan")
        self.camera_scan_button.grid(row=0, column=4, padx=(0, 20), pady=(0, 20), sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Anzeigefläche", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.settings_button = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.open_settings)	
        self.settings_button.grid(row=7, column=0, padx=20, pady=(10, 10))

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Übersicht")
        self.tabview.add("Details")
        self.tabview.add("Augeliehen An")
        self.tabview.tab("Übersicht").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Details").grid_columnconfigure(0, weight=1)



        self.overwiew_tab_label = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Übersicht", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.overwiew_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.overview_tab_bookname = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_bookname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_bookname_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Titel")
        self.overview_tab_bookname_info.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_author = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Autor", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_author_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Autor")
        self.overview_tab_author_info.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_isbn = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="ISBN", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_isbn.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_isbn_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"),text="ISBN")
        self.overview_tab_isbn_info.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_genre = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_genre_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Genre")
        self.overview_tab_genre_info.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_language = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_language_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Sprache")
        self.overview_tab_language_info.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_publisher = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_publisher.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_publisher_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Verlag")
        self.overview_tab_publisher_info.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="nsew")

        self.overview_tab_year = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.overview_tab_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
        self.overview_tab_year_info = customtkinter.CTkLabel(self.tabview.tab("Übersicht"), text="Jahr")
        self.overview_tab_year_info.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="nsew")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("Sidebar Button")

    def open_settings(self):
        print("Settings")
        self.master.switch_frame(NewBookFrame)

        