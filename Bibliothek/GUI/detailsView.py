import customtkinter


class DetailsFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.setup_frame()
        self.item_view_detail= self.get_detail_view_media()
        print(f"{self.master.detail_view_media_type}")
        print(f"Das ist das ausgewählte Item: {self.item_view_detail}")

        self.detailed_view_item_id = self.master.detail_view_media

        self.setup_widgets()

    def setup_frame(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch"  , command=lambda: self.master.switch_frame(self.master.new_book_frame))
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
        self.tabview = customtkinter.CTkTabview(self, width=1000, height=800 )
        self.tabview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Details")
        self.tabview.add("Zusammenfassung")
        self.tabview.tab("Zusammenfassung").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Zusammenfassung").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Details").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").configure(height=800)

        self.frame_title = customtkinter.CTkLabel(self.tabview, text="Details", font=customtkinter.CTkFont(size=20, weight="bold"))

        

        if self.master.detail_view_media_type == "book":
            self.overview_tab_bookname = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_bookname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_bookname_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[1])
            self.overview_tab_bookname_info.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_author = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Autor", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_author_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[2])
            self.overview_tab_author_info.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_isbn = customtkinter.CTkLabel(self.tabview.tab("Details"), text="ISBN", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_isbn.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_isbn_info = customtkinter.CTkLabel(self.tabview.tab("Details"),text=self.book[5])
            self.overview_tab_isbn_info.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_genre = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_genre_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[6])
            self.overview_tab_genre_info.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_language = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_language_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[7])
            self.overview_tab_language_info.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_publisher = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_publisher.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_publisher_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[8])
            self.overview_tab_publisher_info.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_year = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_year_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[3])
            self.overview_tab_year_info.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_pages = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Seiten", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_pages.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_pages_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.book[9])
            self.overview_tab_pages_info.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_spaceholder = customtkinter.CTkLabel(self.tabview.tab("Details"), text="", fg_color="transparent", bg_color="transparent")
            self.overview_spaceholder.grid(row=9, column=0, padx=20, pady=(20, 10), sticky="w")

            self.overview_spaceholder1 = customtkinter.CTkLabel(self.tabview.tab("Details"), text="", fg_color="transparent", bg_color="transparent")
            self.overview_spaceholder1.grid(row=10, column=0, padx=20, pady=(20, 10), sticky="w")

            self.overview_spaceholder2 = customtkinter.CTkLabel(self.tabview.tab("Details"), text="", fg_color="transparent", bg_color="transparent")
            self.overview_spaceholder2.grid(row=11, column=0, padx=20, pady=(20, 10), sticky="w")

            self.overview_spaceholder3 = customtkinter.CTkLabel(self.tabview.tab("Details"), text="", fg_color="transparent", bg_color="transparent")
            self.overview_spaceholder3.grid(row=12, column=0, padx=20, pady=(20, 10), sticky="w")

            self.overview_spaceholder4 = customtkinter.CTkLabel(self.tabview.tab("Details"), text="", fg_color="transparent", bg_color="transparent")
            self.overview_spaceholder4.grid(row=13, column=0, padx=20, pady=(20, 10), sticky="w")

        elif self.master.detail_view_media_type == "Film":
            pass
        elif self.master.detail_view_media_type == "Game":
            pass
        
        self.zusammenfassung_tab_label = customtkinter.CTkLabel(self.tabview.tab("Zusammenfassung"), text="Zusammenfassung", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.zusammenfassung_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nw")
        self.zusammenfassung_tab_text = customtkinter.CTkTextbox(self.tabview.tab("Zusammenfassung"), width=800, height=800)
        description_text = str(self.item_view_detail.description) if self.item_view_detail.description is not None else ""
        self.zusammenfassung_tab_text.insert("1.0", description_text)

        self.zusammenfassung_tab_text.configure(state="disabled")
        self.zusammenfassung_tab_text.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

    
    def get_detail_view_media(self):
        if self.master.detail_view_media_type != None:
            item_details = self.master.bibliothek.get_media_by_id_and_type(self.master.detail_view_media, self.master.detail_view_media_type)
            return item_details
        else:
            pass

    def open_settings(self):
        pass