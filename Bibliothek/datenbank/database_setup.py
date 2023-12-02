import sqlite3

def create_database():
    conn = sqlite3.connect('Library.db')
    cursor = conn.cursor()

    # Tabelle für Bücher
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            publication_year INTEGER
        )
    ''')

    # Tabelle für Filme
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            director TEXT,
            genre TEXT,
            release_year INTEGER
        )
    ''')

    # Tabelle für Spiele
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            title TEXT,
            developer TEXT,
            genre TEXT,
            platform TEXT
        )
    ''')

    # Tabelle für Benutzer
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    ''')
    print("Alles hat geworked")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
