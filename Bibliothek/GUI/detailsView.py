from datetime import datetime, timedelta
import customtkinter
from ..datenmodelle import medien

class DetailsFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, item,  **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.item:medien.Medien = item

        print(f"Setting up details frame")
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
        self.tabview = customtkinter.CTkTabview(self, width=1000, height=800 )
        self.tabview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Details")
        self.tabview.add("Zusammenfassung")
        self.tabview.tab("Zusammenfassung").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Zusammenfassung").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").grid_rowconfigure(0, weight=1)
        self.tabview.tab("Details").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Details").configure(height=800)


        if self.item.borrowed:
            self.tabview.add("Ausgeliehen")
            self.tabview.tab("Ausgeliehen").grid_rowconfigure(0, weight=1)
            self.tabview.tab("Ausgeliehen").grid_columnconfigure(0, weight=1)
            print("Ausgeliehen")

        print(f"Das ist item in detailsView.py: {self.item}")
        self.frame_title = customtkinter.CTkLabel(self.tabview, text="Details", font=customtkinter.CTkFont(size=20, weight="bold"))

        if type(self.item) == medien.Buch:
            self.build_book()
        elif type(self.item) == medien.Film:
            self.build_film()
        elif type(self.item) == medien.Spiel:
            self.build_game()

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

        self.bearbeiten_button = customtkinter.CTkButton(self.tabview.tab("Details"), text="Bearbeiten", command=self.change_to_edit_media_frame)
        self.bearbeiten_button.grid(row=14, column=0, padx=20, pady=(10, 10), sticky="w")

        self.ausleihen_button = customtkinter.CTkButton(self.tabview.tab("Details"), text="Ausleihen An", command=lambda: self.media_borrow_dialog())
        self.ausleihen_button.grid(row=14, column=1, padx=20, pady=(10, 10), sticky="e")

        self.delete_button = customtkinter.CTkButton(self.tabview.tab("Details"), text="Löschen", command=lambda: self.delete_media_dialog())
        self.delete_button.grid(row=14, column=2, padx=20, pady=(10, 10), sticky="e")

        
        self.zusammenfassung_tab_label = customtkinter.CTkLabel(self.tabview.tab("Zusammenfassung"), text="Zusammenfassung", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.zusammenfassung_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nw")
        self.zusammenfassung_tab_text = customtkinter.CTkTextbox(self.tabview.tab("Zusammenfassung"), width=800, height=800)
        self.zusammenfassung_tab_text.insert("1.0", str(self.item.description))

        self.zusammenfassung_tab_text.configure(state="disabled")
        self.zusammenfassung_tab_text.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

        if self.item.borrowed:
            borrower = self.get_item_borrowed_by()
            self.ausgeliehen_tab_label = customtkinter.CTkLabel(self.tabview.tab("Ausgeliehen"), text="Ausgeliehen An", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.ausgeliehen_tab_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
            self.ausgeliehen_tab_text = customtkinter.CTkLabel(self.tabview.tab("Ausgeliehen"), text=borrower.name)
            self.ausgeliehen_tab_text.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="nsew")

            self.ausgeliehen_tab_tickbox_zurückgegeben = customtkinter.CTkCheckBox(self.tabview.tab("Ausgeliehen"), text="Zurückgegeben", command=self.change_borrow_status_book )
            self.ausgeliehen_tab_tickbox_zurückgegeben.grid(row=2, column=0, padx=20, pady=(10, 10), sticky="w")

    def build_book(self):
            self.overview_tab_bookname = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_bookname.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_bookname_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.titel)
            self.overview_tab_bookname_info.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_author = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Autor", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_author.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_author_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.autor_oder_regisseur)
            self.overview_tab_author_info.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_isbn = customtkinter.CTkLabel(self.tabview.tab("Details"), text="ISBN", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_isbn.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_isbn_info = customtkinter.CTkLabel(self.tabview.tab("Details"),text=self.item.ESBN)
            self.overview_tab_isbn_info.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_genre = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_genre.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_genre_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.genre)
            self.overview_tab_genre_info.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_language = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_language.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_language_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.language)
            self.overview_tab_language_info.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_publisher = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Verlag", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_publisher.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_publisher_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.publisher)
            self.overview_tab_publisher_info.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_year = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_year.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_year_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.publication_year)
            self.overview_tab_year_info.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_tab_pages = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Seiten", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_tab_pages.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_tab_pages_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.pages)
            self.overview_tab_pages_info.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")
        
    def build_film(self):
            self.overview_film_name_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_name_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_name_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.titel)
            self.overview_film_name_info.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_regisseur_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Regisseur", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_regisseur_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_regisseur_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.autor_oder_regisseur)
            self.overview_film_regisseur_info.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_genre_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))  
            self.overview_film_genre_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_genre_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.genre)
            self.overview_film_genre_info.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_year_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_year_label.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_year_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.publication_year)
            self.overview_film_year_info.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_language_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_language_label.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_language_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.language)
            self.overview_film_language_info.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_duration_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Dauer", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_duration_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_duration_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.duration)
            self.overview_film_duration_info.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_actors_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Schauspieler", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_actors_label.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_actors_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.actors)
            self.overview_film_actors_info.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_film_helpers_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Helfer", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_film_helpers_label.grid(row=8, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_film_helpers_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.helpers)
            self.overview_film_helpers_info.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="w")
    
    def build_game(self):
            self.overview_title_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Titel", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_title_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_titel_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.titel)
            self.overview_titel_info.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_developer_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Entwickler", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_developer_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_developer_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.autor_oder_regisseur)
            self.overview_developer_info.grid(row=2, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_genre_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Genre", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_genre_label.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_genre_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.genre)
            self.overview_genre_info.grid(row=3, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_year_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Jahr", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_year_label.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_year_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.publication_year)
            self.overview_year_info.grid(row=4, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_language_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Sprache", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_language_label.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_language_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.language)
            self.overview_language_info.grid(row=5, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_platform_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Plattform", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_platform_label.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_platform_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.platform)
            self.overview_platform_info.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="w")

            self.overview_multiplayer_label = customtkinter.CTkLabel(self.tabview.tab("Details"), text="Multiplayer", font=customtkinter.CTkFont(size=12, weight="bold"))
            self.overview_multiplayer_label.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="w")
            self.overview_multiplayer_info = customtkinter.CTkLabel(self.tabview.tab("Details"), text=self.item.multiplayer)
            self.overview_multiplayer_info.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="w")

    def change_to_edit_media_frame(self):
        self.master.switch_frame(self.master.edit_media_frame, item=self.item)

    def get_item_borrowed_by(self):
        if type(self.item) == medien.Buch:
            media_type = "book"
        elif type(self.item) == medien.Film:
            media_type = "film"
        elif type(self.item) == medien.Spiel:
            media_type = "game" 
        borrowed_media = self.master.bibliothek.get_borrowed_media_by_id(media_id=self.item.id, media_type=media_type)
        customer = self.master.bibliothek.get_customer_by_id(customer_id=borrowed_media.customer_id)
        return customer

    def delete_media_dialog(self):
        if type(self.item) == medien.Buch:
            media_type = "book"
        elif type(self.item) == medien.Film:
            media_type = "film"
        elif type(self.item) == medien.Spiel:
            media_type = "game"
        self.dialog = customtkinter.CTkInputDialog(title="Löschen", text="Sind Sie sicher, dass Sie das Medium löschen möchten? (Ja/Nein)")
        if self.dialog.get_input() == "Ja":
            self.master.bibliothek.delete_media_by_id(media_id=self.item.id, media_type=media_type)
            self.master.switch_frame(self.master.start_frame)
         

    def change_borrow_status_book(self):
        self.item.borrowed = False
        if type(self.item) == medien.Buch:
            media_type = "book"
        elif type(self.item) == medien.Film:
            media_type = "film"
        elif type(self.item) == medien.Spiel:
            media_type = "game"
        self.master.bibliothek.update_media(media=self.item, item_type=media_type)
        self.master.bibliothek.return_media_by_id(media_id=self.item.id, media_type=media_type)
        self.master.switch_frame(self.master.start_frame)

    def media_borrow_dialog(self):
        self.dialog = customtkinter.CTkInputDialog(title="Ausleihen", text="Wer möchte das Buch ausleihen?")
        customer_name = self.dialog.get_input()
        customer = self.master.bibliothek.get_customer_by_name(customer_name)
        if type(self.item) == medien.Buch:
            media_type = "book"
        elif type(self.item) == medien.Film:
            media_type = "film"
        elif type(self.item) == medien.Spiel:
            media_type = "game"
        self.borrow_item(item_id=self.item.id, item_type=media_type, customer=customer)

    def borrow_item(self, item_id, item_type, customer):
        end_date = datetime.now() + timedelta(weeks=4)
        customer_id = customer.id
        
        self.master.bibliothek.create_borrowed_media_object(media_id=item_id, media_type=item_type, customer_id= customer_id, borrow_date=datetime.now(), return_date=end_date, zurückgebracht=False)
        self.item.borrowed = True
        if type(self.item) == medien.Buch:
            media_type = "book"
        elif type(self.item) == medien.Film:
            media_type = "film"
        elif type(self.item) == medien.Spiel:
            media_type = "game"
        self.master.bibliothek.update_media(media=self.item, item_type=media_type)
        self.master.go_back()

        



    def open_settings(self):
        pass