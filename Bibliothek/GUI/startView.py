import customtkinter

from  ..datenbank import MediaDbhandler
from .detailsView import DetailsFrame

class ItemFrame(customtkinter.CTkFrame):
    def __init__(self, startframe, master, item, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.startframe = startframe
        self.master = master
        self.item = item
        self.setup_widgets()
        print(f"finished building ItemFrame for: {self.item}")

    def setup_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.name_Button = customtkinter.CTkButton(self, text=self.item.titel, command=self.on_click, anchor="w", fg_color="transparent", bg_color="transparent", hover=True, hover_color="lightgrey", corner_radius=0)
        self.name_Button.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")
        self.author_button = customtkinter.CTkButton(self, text=self.item.autor_oder_regisseur, command=self.on_click, anchor="w", fg_color="transparent", bg_color="transparent", hover=True, hover_color="lightgrey", corner_radius=0)
        self.author_button.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="nsew")
        self.type_button = customtkinter.CTkButton(self, text=self.item.category, command=self.on_click, anchor="w", fg_color="transparent", bg_color="transparent", hover=True, hover_color="lightgrey", corner_radius=0)
        self.type_button.grid(row=0, column=2, padx=20, pady=(10, 0), sticky="nsew")

    def on_click(self):
        self.startframe.show_details(item=self.item)
    


class StartFrame(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.setup_frame()
        self.setup_side_bar()
        self.setup_widgets()

        self.clear_search_results


    def setup_frame(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

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
        

    def setup_widgets(self):
        # Search Entry
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(10, 10), sticky="nsew")

        # Search Button
        self.search_button = customtkinter.CTkButton(self, text="Search", command=self.search_media, width=10, height=50, corner_radius=0)
        self.search_button.grid(row=0, column=3, padx=(0, 20), pady=(10, 20), sticky="nsew")
        # Camera Scan Button
        self.camera_scan_button = customtkinter.CTkButton(self, text="Scan")
        self.camera_scan_button.grid(row=0, column=4, padx=(0, 20), pady=(10, 20), sticky="nsew")



        self.scrollview = customtkinter.CTkScrollableFrame(self, label_text="Suchergebnisse", width=800, height=800)
        self.scrollview.grid(row=1, column=1, columnspan=2 , padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollview.grid_columnconfigure(0, weight=1)
        self.scrollview.grid_rowconfigure(0, weight=1)
        self.table_label = customtkinter.CTkLabel(self.scrollview, text="Titel", anchor="w")
        self.table_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.table_label1 = customtkinter.CTkLabel(self.scrollview, text="Autor", anchor="w")
        self.table_label1.grid(row=0, column=1, padx=20, pady=(10, 0))
        self.table_label2 = customtkinter.CTkLabel(self.scrollview, text="Typ", anchor="w")
        self.table_label2.grid(row=0, column=2, padx=20, pady=(10, 0))

    def search_media(self):
        self.clear_search_results()


        media_items = self.master.bibliothek.search_media(self.entry.get())
        print(f"media_items: {media_items}")
        if media_items is None:
            return
        itemframes = []
        for index, item in enumerate(media_items):
            print(f"building item: {type(item)} - {item}")
            item = ItemFrame(self, self.scrollview, item)
            itemframes.append(item)
            item.grid(row=index+1, column=0, columnspan=3, padx=20, pady=(10, 0), sticky="nsew")
        print("finished building itemframes", itemframes)


    def show_details(self, item):
        self.master.switch_frame(self.master.detail_view_frame, item=item)


    def clear_search_results(self):
        for widget in self.scrollview.winfo_children():
            if widget not in [self.table_label, self.table_label1, self.table_label2]:
                print("deleted some widgets")
                widget.destroy()