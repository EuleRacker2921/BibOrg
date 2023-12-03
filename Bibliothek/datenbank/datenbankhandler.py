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

    # Weitere Methoden für Kunden

class CustomerDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_customer(self, name, username, email):
        query = "INSERT INTO customers (name, username, email) VALUES (?,?,?)"
        with self.get_db_connection() as conn:
            conn.execute(query, (name, username, email))
            conn.commit()
            self.close_db_connection()

    def get_customer_by_id(self, id):
        query = "SELECT * FROM customers WHERE id = ?"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query, (id,))
            customer = cursor.fetchall()
            self.close_db_connection()
            return customer
    
    def get_all_customers(self):
        query = "SELECT * FROM customers"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query)
            customers = cursor.fetchall()
            self.close_db_connection()
            return customers
    
    def get_customer_by_name(self, name):
        query = "SELECT * FROM customers WHERE name LIKE ?"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query, (f"%{name}%",))
            customer = cursor.fetchall()
            self.close_db_connection()
            return customer

class MediaDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_media(self, media_data, item_type):
        query = ""
        if item_type == "book":
            query = "INSERT INTO books (title, author, genre, publication_year, description, borrowed, language, ESBN, publisher, pages) VALUES (?,?,?,?,?,0,?,?,?,?)"
        elif item_type == "film":
            query = "INSERT INTO films (title, regisseur, genre, publication_year, description, borrowed, language, duration, actors, helpers) VALUES (?,?,?,?,?,0,?,?,?,?)"
        elif item_type == "game":
            query = "INSERT INTO games (title, developer, genre, publication_year, description, borrowed, language, platform) VALUES (?,?,?,?,?,0,?,?,?,?)"
        with self.get_db_connection() as conn:
            if item_type == "book":
                conn.execute(query, (media_data[0], media_data[1], media_data[2], media_data[3], media_data[4], media_data[5], media_data[7], media_data[6], media_data[8]))
            elif item_type == "film":
                conn.execute(query, (media_data[0], media_data[1], media_data[2], media_data[3], media_data[4], media_data[5], media_data[6], media_data[7], media_data[8], media_data[9]))
            elif item_type == "game":
                conn.execute(query, (media_data[0], media_data[1], media_data[2], media_data[3], media_data[4], media_data[5], media_data[6], media_data[7]))
            conn.commit()
            self.close_db_connection()
    
    def update_media(self, media, item_type):
        item_id = media.id
        item_type = item_type
        if item_type == "book":
            query = "UPDATE books SET title = ?, author = ?, genre = ?, publication_year = ?, description = ?, borrowed = ?, language = ?, ESBN = ?, publisher = ?, pages = ? WHERE id = ?"   
        elif item_type == "film":
            query = "UPDATE films SET title = ?, regisseur = ?, genre = ?, publication_year = ?, description = ?, borrowed = ?, language = ?, duration = ?, actors = ?, helpers = ? WHERE id = ?"
        elif item_type == "game":
            query = "UPDATE games SET title = ?, developer = ?, genre = ?, publication_year = ?, description = ?, borrowed = ?, language = ?, platform = ? WHERE id = ?"
        with self.get_db_connection() as conn:
            if item_type == "book":
                conn.execute(query, (media.titel, media.autor_oder_regisseur, media.genre, media.publication_year, media.description, media.borrowed, media.language, media.ESBN, media.publisher, media.pages, item_id))
            elif item_type == "film":
                conn.execute(query, (media.titel, media.autor_oder_regisseur, media.genre, media.publication_year, media.description, media.borrowed, media.language, media.duration, media.actors, media.helpers, item_id))
            elif item_type == "game":
                conn.execute(query, (media.titel, media.autor_oder_regisseur, media.genre, media.publication_year, media.description, media.borrowed, media.language, media.platform, item_id))
            conn.commit()
            self.close_db_connection()

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
        print(media_type)
        if media_type == "Buch":
            media_type = "book"
        elif media_type == "Film":
            media_type = "film"
        elif media_type == "Game":
            media_type = "game"
        
        with self.get_db_connection() as conn:
            # Bücher suchen
            cursor = conn.execute(f"SELECT * FROM {media_type}s WHERE id = ?", (id,))
            media = cursor.fetchall()
            self.close_db_connection()
            print(f"Das ist die db media Liste {media}")

        return media

    def delete_media_by_id(self, id, media_type):
        with self.get_db_connection() as conn:
            # Bücher suchen
            conn.execute(f"DELETE FROM {media_type}s WHERE id = ?", (id,))
            conn.commit()
            self.close_db_connection()


# Ausgeliehene Medien
class BorrowedMediaDbhandler(Datenbank):
    def borrow_media(self, customer_id, media_id, media_type, start_date, end_date, zurückgebracht):
        query = ""
        if media_type == "book":
            query = "UPDATE books SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ?, zurückgebracht = 0 WHERE id = ?"
        elif media_type == "film":
            query = "UPDATE films SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ?, zurückgebracht = 0 WHERE id = ?"
        elif media_type == "game":
            query = "UPDATE games SET borrowed = 1, borrowed_by = ?, borrow_start_date = ?, borrow_end_date = ?, zurückgebracht = 0 WHERE id = ?"

        if query:
            with self.get_db_connection() as conn:
                conn.execute(query, (customer_id, start_date, end_date, media_id))
                conn.commit()
                self.close_db_connection()

    def return_media(self, media_id, media_type):
        query = ""
        if media_type == "book":
            query = "UPDATE books SET borrowed = 0 WHERE id = ?"
        elif media_type == "film":
            query = "UPDATE films SET borrowed = 0 WHERE id = ?"
        elif media_type == "game":
            query = "UPDATE games SET borrowed = 0 WHERE id = ?"

        if query:
            with self.get_db_connection() as conn:
                conn.execute(query, (media_id,))
                conn.execute("UPDATE borrowed_media SET zurückgebracht = 1 WHERE media_id = ? AND media_type = ?", (media_id, media_type))
                conn.commit()
                self.close_db_connection()

    
    def create_borrowed_media(self, borrowed_media):
        query = "INSERT INTO borrowed_media (media_id,  media_type, customer_id, borrow_date, return_date, zurückgebracht) VALUES (?,?,?,?,?, 0)"
        with self.get_db_connection() as conn:
            media_id = borrowed_media.media_id
            media_type = borrowed_media.media_type
            customer_id = borrowed_media.customer_id
            borrow_date = borrowed_media.borrow_date
            return_date = borrowed_media.return_date
            print(f"Das ist die media_id: {media_id}, media_type: {media_type}, customer_id: {customer_id}, borrow_date: {borrow_date}, return_date: {return_date}")
            conn.execute(query, (media_id, media_type,customer_id, borrow_date, return_date))
            conn.commit()
            self.close_db_connection()

    def get_borrowed_media_by_id(self, media_id, media_type):
        query = "SELECT * FROM borrowed_media WHERE media_id = ? AND media_type = ? AND zurückgebracht = 0"
        with self.get_db_connection() as conn:
            cursor = conn.execute(query, (media_id, media_type))
            borrowed_media = cursor.fetchall()
            print(f"Das ist die borrowed_media Liste {borrowed_media}")
            self.close_db_connection()
            return borrowed_media
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
            
            
        
