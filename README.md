# BibOrg
Schule Ersatzleistung Objectorientiert Bibliothekmanager


# Genaue Aufgabenstellung
    
Entwickle ein kleines Programm in Python, das innerhalb deines Oberthemas verwendet werden kann.

Verwende in deinem Code die grundlegende Konzepte der objektorientierten Programmierung (Klassen, Instanzen [Objekte einer Klasse], Methoden [einer Klasse], Vererbung, Modularisierung).

Du hast die Wahl zwischen zwei Themen:
- Gleichungen/Gleichungssysteme lösen
oder
- Bibliothek

# Credits
[customtkinter von Tom Schimansky](https://github.com/TomSchimansky/CustomTkinter)


# Was zu sehen ist
- `Bibliothek` ist das Hauptverzeichnis
- `vereinfachteAufgabe.py` ist als kleinere Version ein CMD Programm
- `vereinfachteAufgabetest.py` ist das Testscript für `vereinfachteAufgabe.py`
- `./UML` enthält alle UML Diagramme vom Project
- `./pics` enthält ein Prove, dass die Camera Barcode erkennung funktioniert

# Anleitung
INFO: beste Funktion auf Windows
INFO: Folgende Funktionen sind noch nicht voll nutzbar:
- Camera Scan Barcode --> scant zwar wird aber nicht verarbeitet
- Favourite Buttons
- Settings Button bzw Das Frame
    - Soll Anzeigemodus einstellen können
        - Dark
        - White
        - System
    - GUI Größe anpassbar machen
    - Favourites Einstellbar machen
    - User Verwaltung
    - usw    


1. Das Repo herunterladen
2. Ein Virtual Enviroment erstellen

```bash
python -m venv venv
```

4. Venv  aktivieren
Windows:

```bash
./venv/Scripts/activate
```

MacOs:

```bash
source venv/bin/activate
```

5. Dependecys herunterladen

```bash
pip install -r requirements.txt
```

7. Im Ordner BIBORG bzw im Übergeordneten Ordner `BIBORG`
```bash
python -m Bibliothek
```
8. Anmelden mit Benutzername: `admin` pwd: `admin`
