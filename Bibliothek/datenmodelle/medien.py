class Medien:
    def __init__(self, id, titel, autor_oder_regisseur=None, genre=None, publication_year=None, description=None, borrowed=None, language=None, category=None):
        self.id = id
        self.titel = titel
        self.autor_oder_regisseur = autor_oder_regisseur
        self.genre = genre
        self.publication_year = publication_year
        self.description = description  
        self.language = language
        self.borrowed = borrowed
        self.category = category

    def ausleihen(self):
        if not self.borrowed:
            self.borrowed = True
            return True
        else:
            return False

    def zurueckgeben(self):
        self.borrowed = False


    def __str__(self):
        return f"{self.titel} von {self.autor_oder_regisseur}, Genre: {self.genre}, {'Ausgeliehen' if self.borrowed else 'Verfügbar'}"

class Buch(Medien):
    def __init__(self, id, titel, autor_oder_regisseur, genre, publication_year, description, borrowed, ESBN, language,  publisher, pages, category="Buch"):
        super().__init__(id, titel, autor_oder_regisseur, genre, publication_year, description, borrowed, language, category)
        self.publisher = publisher
        self.ESBN = ESBN
        self.pages = pages

    def calculate_reading_time(self):
        return self.pages / 100 * 60 # angenommen man ließt 100 Seiten pro Stunde

class Film(Medien):
    def __init__(self, id, titel, regisseur=None, genre=None, publication_year=None, description=None, borrowed=False, language=None, duration=None, actors=None, helpers=None, category="Film"):
        super().__init__(id, titel, regisseur, genre, publication_year, description, borrowed, language, category)
        self.duration = duration
        self.actors = actors
        self.helpers = helpers

    def printcredits(self):
        print("Hauptdarsteller:")
        for actor in self.actors:
            print(actor)
        print("Nebendarsteller:")
        for helper in self.helpers:
            print(helper)
    
    def creditslist(self):
        return self.actors + self.helpers
    
class Spiel(Medien):
    def __init__(self, id, titel, entwickler, genre, publication_year, description, borrowed, language, platform, multiplayer, average_playtime, category="Game"):
        super().__init__(id, titel, entwickler, genre, publication_year, description, borrowed, language, category)
        self.platform = platform
        self.multiplayer = multiplayer
        self.average_playtime = average_playtime

    def getrecommendedpcspecs(self):
        return "GTX 1080, i7 8700k, 16GB RAM, 1TB SSD"
