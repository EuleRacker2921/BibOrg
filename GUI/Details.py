import customtkinter

from book_bearbeiten import book_bearbeiten_Frame
from new_book import NewBookFrame
from dbhandler import booksDbhandler, borrowedBooksDbhandler, customerDbhandler


class DetailsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.book = self.get_book(self.master.detail_view_book)

        self.setup_side_bar()
        self.setup_details_tab()

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

    def setup_details_tab(self):
        self.tabview = customtkinter.CTkTabview(self, width=1000, height=800 )
        self.tabview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Details")
        self.tabview.add("Zusammenfassung")
        self.tabview.tab("Zusammenfassung").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Zusammenfassung").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Details").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").configure(height=800)

        if self.book[10] == 1:
            self.tabview.add("Ausgeliehen")
            self.tabview.tab("Ausgeliehen").grid_rowconfigure(0, weight=1)
            self.tabview.tab("Ausgeliehen").grid_columnconfigure(0, weight=1)
            print("Ausgeliehen")

        self.overwiew_tab_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Details", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.overwiew_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

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

        self.bearbeiten_button = customtkinter.CTkButton(self.tabview.tab("Details"), text="Bearbeiten", command=self.switch_frame_book_bearbeiten_Frame)
        self.bearbeiten_button.grid(row=14, column=0, padx=20, pady=(10, 10), sticky="w")

        self.delete_button = customtkinter.CTkButton(self.tabview.tab("Details"), text="Löschen", command=self.delete_book)
        self.delete_button.grid(row=14, column=1, padx=20, pady=(10, 10), sticky="e")


        self.zusammenfassung_tab_label = customtkinter.CTkLabel(self.tabview.tab("Zusammenfassung"), text="Zusammenfassung", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.zusammenfassung_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nw")
        self.zusammenfassung_tab_text = customtkinter.CTkTextbox(self.tabview.tab("Zusammenfassung"), width=800, height=800)
        self.zusammenfassung_tab_text.insert("1.0", self.book[4])
        self.zusammenfassung_tab_text.configure(state="disabled")
        self.zusammenfassung_tab_text.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

        if self.book[10] == 1:
            self.ausgeliehen_tab_label = customtkinter.CTkLabel(self.tabview.tab("Ausgeliehen"), text="Ausgeliehen An", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.ausgeliehen_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
            self.ausgeliehen_tab_text = customtkinter.CTkLabel(self.tabview.tab("Ausgeliehen"), text=self.get_ausleiher_book(self.book[0]))
            self.ausgeliehen_tab_text.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="nsew")

            self.ausgeliehen_tab_tickbox_zurückgegeben = customtkinter.CTkCheckBox(self.tabview.tab("Ausgeliehen"), text="Zurückgegeben", command=self.change_borrow_status_book )
            self.ausgeliehen_tab_tickbox_zurückgegeben.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="w")

    def change_borrow_status_book(self):
        booksdb = booksDbhandler()
        booksdb.change_borrow_status_book(self.book[0])
        borrowedbooksdb = borrowedBooksDbhandler()
        borrowedbooksdb.change_borrow_status_book(self.book[0], 1)
        self.master.go_back()



    def get_ausleiher_book(self, book_id):
        customerdb = customerDbhandler()
        booksdb = borrowedBooksDbhandler()
        ausgeliehendes_book = booksdb.get_borrowed_book(book_id)
        if ausgeliehendes_book is not None:
            ausleiher = ausgeliehendes_book[1]
            ausleihername = customerdb.get_customer(ausleiher)
            print(ausleihername[1])
            return ausleihername[1]
        else:
            return None

    def get_book(self, book_id):
        booksdb = booksDbhandler()
        book = booksdb.get_book(book_id)
        return book

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        self.master.switch_frame(NewBookFrame)

    def back_button_event(self):
        self.master.go_back()

    def open_settings(self):
        print("Settings")
        
    def switch_frame_book_bearbeiten_Frame(self):
        self.master.switch_frame(book_bearbeiten_Frame)

    def delete_book(self):
        booksdb = booksDbhandler()
        booksdb.delete_book(self.book[0])
        self.master.go_back()

        