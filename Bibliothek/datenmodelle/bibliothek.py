from .medien import Buch, Film, Spiel, BorrowedMedia
from .customer import Customer

from ..datenbank import MediaDbhandler, BorrowedMediaDbhandler, CustomerDbhandler

class Bibliothek:
    def __init__(self):
        self.medien = []
        self.detail_media = None 


    def add_customer(self, name, username, email):
        print("add customer")
        db = CustomerDbhandler()
        db.add_customer(name, username, email)


    def return_media_by_id(self, media_id, media_type):
        print("return media")
        db = BorrowedMediaDbhandler()
        db.return_media(media_id, media_type)

    def update_media(self, media, item_type):
        print("update media")
        db = MediaDbhandler()
        db.update_media(media, item_type)

    def get_borrowed_media_by_id(self, media_id, media_type):
        print("get borrowed media by id")
        db = BorrowedMediaDbhandler()
        result = db.get_borrowed_media_by_id(media_id, media_type)
        print(result)
        id, media_id, media_type, customer_id, borrow_date, return_date, zurückgebracht = result[0]
        borrowedMedia = BorrowedMedia(media_id, media_type, customer_id, borrow_date, return_date, zurückgebracht)
        return borrowedMedia

    def get_customer_by_id(self, customer_id):
        print("get customer by id")
        db = CustomerDbhandler()
        result = db.get_customer_by_id(customer_id)
        created_customer = self.create_customer_object(result)
        return created_customer


    def delete_media_by_id(self, media_id, media_type):
        print("delete media by id")
        db = MediaDbhandler()
        db.delete_media_by_id(media_id, media_type)

    def get_customer_by_name(self, name):
        print("get customer by name")
        db = CustomerDbhandler()
        result = db.get_customer_by_name(name)
        created_customer = self.create_customer_object(result)
        return created_customer

    def create_customer_object(self, customer_data):
        print("create customer object")
        
        customer_id, name, username, email = customer_data[0]
        customer = Customer(customer_id, name, username, email)
        return customer

    def create_borrowed_media_object(self, media_id,media_type, customer_id, borrow_date, return_date, zurückgebracht):
        borrowedMedia = BorrowedMedia(media_id,media_type, customer_id, borrow_date, return_date, zurückgebracht)
        db = BorrowedMediaDbhandler()
        db.create_borrowed_media(borrowedMedia)
        return borrowedMedia

    def get_media_by_id_and_type(self, myid, media_type):
        print("get media by id and type")

        db = MediaDbhandler()
        result = db.get_media_by_id_and_type(myid, media_type)
        self.create_media_objects(result)
        print("finished creating media objects")
        self.detail_media = result
        return self.detail_media

    def search_media(self, search_term):
        self.medien.clear()
        print("Alte Medien gelöscht. Starte neue Suche.")
        
        db = MediaDbhandler()
        results = db.search_engine_for_media(search_term)
        print(f"Suchergebnisse: {results}")
        
        self.create_media_objects(results)
        return self.medien

    def create_media_objects(self, media_data):
        
        for media_type, *data in media_data:
            print(media_type, *data)
            media_id = data[0]  # Annahme, dass die ID immer das erste Element in data ist
            if not self.check_if_media_exists(media_id, media_type):
                if media_type == 'book':
                    print("creating book")
                    self.medien.append(Buch(*data))
                elif media_type == 'film':
                    print("creating film")
                    self.medien.append(Film(*data))
                elif media_type == 'game':
                    print("creating game")
                    self.medien.append(Spiel(*data))


    def check_if_media_exists(self, media_id, media_type):
        for medium in self.medien:
            if isinstance(medium, Buch) and media_type == 'book' and medium.id == media_id:
                return True
            elif isinstance(medium, Film) and media_type == 'film' and medium.id == media_id:
                return True
            elif isinstance(medium, Spiel) and media_type == 'game' and medium.id == media_id:
                return True
        return False