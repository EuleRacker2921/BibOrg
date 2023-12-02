class Medien:
    def __init__(self, titel, autor_oder_regisseur, genre):
        self.titel = titel
        self.autor_oder_regisseur = autor_oder_regisseur
        self.genre = genre
        self.ausgeliehen = False

    def ausleihen(self):
        if not self.ausgeliehen:
            self.ausgeliehen = True
            return True
        else:
            return False

    def zurueckgeben(self):
        self.ausgeliehen = False

    def __str__(self):
        return f"{self.titel} von {self.autor_oder_regisseur}, Genre: {self.genre}, {'Ausgeliehen' if self.ausgeliehen else 'Verfügbar'}"

class Buch(Medien):
    def __init__(self, titel, autor, genre):
        super().__init__(titel, autor, genre)

class Film(Medien):
    def __init__(self, titel, regisseur, genre, laufzeit):
        super().__init__(titel, regisseur, genre)
        self.laufzeit = laufzeit

    def __str__(self):
        return super().__str__() + f", Laufzeit: {self.laufzeit} Minuten"

class Spiel(Medien):
    def __init__(self, titel, entwickler, genre, plattform):
        super().__init__(titel, entwickler, genre)
        self.plattform = plattform

    def __str__(self):
        return super().__str__() + f", Plattform: {self.plattform}"

class Bibliothek:
    def __init__(self):
        self.medien = []

    def medium_hinzufuegen(self, medium):
        self.medien.append(medium)

    def medium_entfernen(self, titel):
        self.medien = [medium for medium in self.medien if medium.titel != titel]

    def medium_suchen(self, titel):
        for medium in self.medien:
            if medium.titel == titel:
                return medium
        return None

    def medien_anzeigen(self):
        for medium in self.medien:
            print(medium)

