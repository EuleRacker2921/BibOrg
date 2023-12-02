import sqlite3

class Datenbank:
    def __init__(self) -> None:
        self.DATABASE_PATH = "Bibliothek/datenbank/Library.db"
        self.get_db_connection()

    def get_db_connection(self):
        cursor = sqlite3.connect(self.DATABASE_PATH)
        return cursor
    
    def close_db_connection(self):
        self.get_db_connection().close()
        print("Verbindung zur Datenbank geschlossen")

# Bücher
class BooksDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_book(self, title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed):
        query = "INSERT INTO books (title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed) VALUES (?,?,?,?,?,?,?,?,?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed))
            conn.commit()
            self.close_db_connection()

    def delete_book(self, id):
        query = "DELETE FROM books WHERE id = ?"
        with self.get_db_connection() as conn:
            conn.execute(query, (id,))
            conn.commit()
            self.close_db_connection()

    def update_book(self, id, title, author, publication_year, description, ESBN, genre, language, publisher, pages):
        query = "UPDATE books SET title = ?, author = ?, publication_year = ?, description = ?, ESBN = ?, genre = ?, language = ?, publisher = ?, pages = ? WHERE id = ?"
        with self.get_db_connection() as conn:
            conn.execute(query, (title, author, publication_year, description, ESBN, genre, language, publisher, pages, id))
            conn.commit()
            self.close_db_connection()

    def get_all_books(self):
        query = "SELECT * FROM books"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query)
            books = cursor.fetchall()
            self.close_db_connection()
            return books
    
    def get_book_by_id(self, id):
        query = "SELECT * FROM books WHERE id = ?"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query, (id,))
            book = cursor.fetchone()
            self.close_db_connection()
            return book
    

    # Weitere Methoden für Bücher

# Filme
class FilmsDbhandler(Datenbank):
    def __init__(self):
        super().__init__()
    def add_film(self, title, director, release_year, description, genre, language, duration, borrowed):
        query = "INSERT INTO films (title, director, release_year, description, genre, language, duration, borrowed) VALUES (?,?,?,?,?,?,?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (title, director, release_year, description, genre, language, duration, borrowed))
            conn.commit()
            self.close_db_connection()

    # Weitere Methoden für Filme

# Spiele
class GamesDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_game(self, title, developer, release_year, genre, platform, borrowed):
        query = "INSERT INTO games (title, developer, release_year, genre, platform, borrowed) VALUES (?,?,?,?,?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (title, developer, release_year, genre, platform, borrowed))
            conn.commit()
            self.close_db_connection()

    # Weitere Methoden für Spiele

# Kunden
class CustomerDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_customer(self, name, address, phone, email, username, password, age):
        query = "INSERT INTO customer (name, address, phone, email, username, password, age) VALUES (?,?,?,?,?,?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (name, address, phone, email, username, password, age))
            conn.commit()
            self.close_db_connection()

    # Weitere Methoden für Kunden

class MediaDbhandler(Datenbank):
    def __init__(self):
        super().__init__()
    
    def get_all_media(self):
        query = "SELECT * FROM books UNION SELECT * FROM films UNION SELECT * FROM games"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query)
            media = cursor.fetchall()
            self.close_db_connection()
            return media
    
    def search_engine_for_media(self, search_term):
        media = []
        with self.get_db_connection() as conn:
            # Bücher suchen
            cursor = conn.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ? OR publication_year LIKE ? OR description LIKE ? OR ESBN LIKE ?  OR language LIKE ? OR publisher LIKE ? OR pages LIKE ?", (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
            books = [('book', *row) for row in cursor.fetchall()]
            
            # Filme suchen
            cursor = conn.execute("SELECT * FROM films WHERE title LIKE ? OR regisseur LIKE ? OR genre LIKE ? OR publication_year LIKE ? OR description LIKE ? OR language LIKE ? OR duration LIKE ? OR actors LIKE ? OR helpers LIKE ?", (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
            films = [('film', *row) for row in cursor.fetchall()]
            
            # Spiele suchen
            cursor = conn.execute("SELECT * FROM games WHERE title LIKE ? OR developer LIKE ? OR genre LIKE ? OR publication_year LIKE ? OR description LIKE ? OR language LIKE ? OR platform LIKE ?", (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%",  f"%{search_term}%", f"%{search_term}%"))
            games = [('game', *row) for row in cursor.fetchall()]

            media.extend(books)
            media.extend(films)
            media.extend(games)
            print(f"Das ist die db media Liste {media}")
            self.close_db_connection()

        return media

    def get_media_by_id_and_type(self, id, media_type):
        media = []
        with self.get_db_connection() as conn:
            # Bücher suchen
            cursor = conn.execute(f"SELECT * FROM {media_type}s WHERE id = ?", (id,))
            media = [(media_type, *row) for row in cursor.fetchall()]
            self.close_db_connection()
            print(media)

        return media


# Ausgeliehene Medien
class BorrowedMediaDbhandler(Datenbank):
    def borrow_media(self, customer_id, media_id, media_type, start_date, end_date):
        query = ""
        if media_type == "book":
            query = "UPDATE books SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ? WHERE id = ?"
        elif media_type == "film":
            query = "UPDATE films SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ? WHERE id = ?"
        elif media_type == "game":
            query = "UPDATE games SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ? WHERE id = ?"

        if query:
            with self.get_db_connection() as conn:
                conn.execute(query, (customer_id, start_date, end_date, media_id))
                conn.commit()
                self.close_db_connection()

    def return_media(self, media_id, media_type):
        query = ""
        if media_type == "book":
            query = "UPDATE books SET borrowed = 0, borrowed_by = NULL, borrow_start_date = NULL, borrow_end_date = NULL WHERE id = ?"
        elif media_type == "film":
            query = "UPDATE films SET borrowed = 0, borrowed_by = NULL, borrow_start_date = NULL, borrow_end_date = NULL WHERE id = ?"
        elif media_type == "game":
            query = "UPDATE games SET borrowed = 0, borrowed_by = NULL, borrow_start_date = NULL, borrow_end_date = NULL WHERE id = ?"

        if query:
            with self.get_db_connection() as conn:
                conn.execute(query, (media_id,))
                conn.commit()
                self.close_db_connection()

    # Weitere Methoden...

# Benutzer
class UsersDbhandler(Datenbank):
    def __init__(self):
        super().__init__()
    # Methoden für Benutzerverwaltung
    def add_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (username, password))
            conn.commit()
            self.close_db_connection()

    
    def validate_user(self, username, password):
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query, (username, password))
            if cursor.fetchone():
               self.close_db_connection()
               return True
            
            else:
                self.close_db_connection()
                return False 
            
            
        