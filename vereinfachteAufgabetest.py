from vereinfachteAufgabe import *

meine_bibliothek = Bibliothek()
meine_bibliothek.medium_hinzufuegen(Buch("Python Programmierung", "Max Mustermann", "Informatik"))
meine_bibliothek.medium_hinzufuegen(Film("Inception", "Christopher Nolan", "Sci-Fi", 148))
meine_bibliothek.medium_hinzufuegen(Spiel("The Witcher 3", "CD Projekt", "RPG", "PC"))

print("Verfügbare Medien:")
meine_bibliothek.medien_anzeigen()

medium = meine_bibliothek.medium_suchen("Inception")
if medium:
    medium.ausleihen()

print("\nNach dem Ausleihen:")
meine_bibliothek.medien_anzeigen()