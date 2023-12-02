import customtkinter

from Details import DetailsFrame
from settings import settings_view_Frame
from new_book import NewBookFrame
from dbhandler import booksDbhandler
from new_customer import NewCustomerFrame

class StartSiteFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


        self.selected_books = None
        self.master.detail_view_book = None

        self.setup_side_bar()

        

        # Search Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(10, 10), sticky="nsew")

        # Search Button
        self.search_button = customtkinter.CTkButton(self, text="Search", command=self.search_books, width=10, height=50, corner_radius=0)
        self.search_button.grid(row=0, column=3, padx=(0, 20), pady=(10, 20), sticky="nsew")
        # Camera Scan Button
        self.camera_scan_button = customtkinter.CTkButton(self, text="Scan")
        self.camera_scan_button.grid(row=0, column=4, padx=(0, 20), pady=(10, 20), sticky="nsew")



        self.scrollview = customtkinter.CTkScrollableFrame(self, label_text="Suchergebnisse", width=800, height=800)
        self.scrollview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollview.grid_columnconfigure(0, weight=1)
        self.scrollview.grid_rowconfigure(0, weight=1)
        self.table_label = customtkinter.CTkLabel(self.scrollview, text="Buchname", anchor="w")
        self.table_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.table_label1 = customtkinter.CTkLabel(self.scrollview, text="Autor", anchor="w")
        self.table_label1.grid(row=0, column=1, padx=20, pady=(10, 0))



    def setup_side_bar(self):
        
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=280 , corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)
        # Logo
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bücherei", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Neues Buch"  , command=lambda: self.master.switch_frame(NewBookFrame))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Neuer Kunde", command=lambda: self.master.switch_frame(NewCustomerFrame))
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



    def search_books(self):
        booksdb = booksDbhandler()
        search_text = self.entry.get()
        self.selected_books = booksdb.search_for_books(search_text)
        
        self.clear_search_results()  # Clear previous search results

        if self.selected_books is not None:
            for idx, book in enumerate(self.selected_books):
                book_name_button = customtkinter.CTkButton(self.scrollview, text=book[1], anchor="w", bg_color="transparent", command=lambda: self.select_detail_book(book[0]), fg_color="transparent", border_width=0, hover=True, hover_color="#e0e0e0", )
                book_name_button.grid(row=idx, column=0, padx=20, pady=(10, 0), sticky="nw")
                book_author_label = customtkinter.CTkLabel(self.scrollview, text=book[2], anchor="w")
                book_author_label.grid(row=idx, column=1, padx=20, pady=(10, 0))
        else:
            print("No books found.")
        
    def select_detail_book(self, book_id):
        self.master.detail_view_book = book_id
        self.master.switch_frame(DetailsFrame)


    def back_button_event(self):
        self.master.go_back()


    def clear_search_results(self):
        for widget in self.scrollview.winfo_children():
            widget.destroy()


    def sidebar_button_event(self):
        self.master.switch_frame(NewBookFrame)

    def open_settings(self):
        print("Settings")
        self.master.switch_frame(NewBookFrame)

        