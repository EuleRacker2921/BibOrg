from .medien import Buch, Film, Spiel

from ..datenbank import MediaDbhandler

class Bibliothek:
    def __init__(self):
        self.medien = []
        self.detail_media = None 

    def medium_hinzufuegen(self, medium):
        self.medien.append(medium)

    def medium_entfernen(self, titel):
        self.medien = [medium for medium in self.medien if medium.titel != titel]


    def get_media_by_id_and_type(self, id, media_type):
        print("get media by id and type")

        db = MediaDbhandler()
        result = db.get_media_by_id_and_type(id, media_type)
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

    def medium_hinzufuegen(self, medium):
        self.medien.append(medium)

    def medium_entfernen(self, titel):
        self.medien = [medium for medium in self.medien if medium.titel != titel]

    def search_media(self, search_term):
        # Hier rufen Sie die Suchfunktion aus Ihrem Datenbankhandler auf
        db = MediaDbhandler()
        results = db.search_engine_for_media(search_term)
        self.create_media_objects(results)
        print(self.medien)
        return self.medien
        # Weitere Logik, um die Suchergebnisse zu verarbeiten oder zurückzugeben