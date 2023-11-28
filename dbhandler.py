import sqlite3

class Datenbank():
    def __init__(self):
        self.db = sqlite3.connect("datenbank.db")
        self.cursor = self.db.cursor()

    def test_connection(self):
        if self.db:
            return True
        else:
            return False

    def close(self):
        self.db.close()

class customerDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_customer(self, name, address, phone, email, username, password, age):
        self.cursor.execute("INSERT INTO customer (name, address, phone, email, username, password, age) VALUES (?,?,?,?,?,?,?)", (name, address, phone, email, username, password, age))
        self.db.commit()

    def update_customer(self, id, name, address, phone, email, username, password, age):
        self.cursor.execute("UPDATE customer SET name=?, address=?, phone=?, email=?, username=?, password=?, age=? WHERE id=?", (name, address, phone, email, username, password, age, id))
        self.db.commit()

    def delete_customer(self, id):
        self.cursor.execute("DELETE FROM customer WHERE id=?", (id,))
        self.db.commit()

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM customer")
        return self.cursor.fetchall()

    def get_customer(self, id):
        self.cursor.execute("SELECT * FROM customer WHERE id=?", (id,))
        return self.cursor.fetchone()

    
class booksDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_book(self, title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed):
        self.cursor.execute("INSERT INTO books (title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed) VALUES (?,?,?,?,?,?,?,?,?,?)", (title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed))
        self.db.commit()

    def update_book(self, id, title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed):
        self.cursor.execute("UPDATE books SET title=?, author=?, publication_year=?, description=?, ESBN=?, genre=?, language=?, publisher=?, pages=?, borrowed=? WHERE id=?", (title, author, publication_year, description, ESBN, genre, language, publisher, pages, borrowed, id))
        self.db.commit()

    def delete_book(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.db.commit()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_book(self, id):
        self.cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        return self.cursor.fetchone()

    def get_borrowed_books(self):
        self.cursor.execute("SELECT * FROM borrowed_books")
        return self.cursor.fetchall()

class borrowedBooksDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_borrowed_book(self, customer_id, book_id, start_date, end_date):
        self.cursor.execute("INSERT INTO borrowed_books (customer_id, book_id, start_date, end_date) VALUES (?,?,?,?)", (customer_id, book_id, start_date, end_date))
        self.db.commit()

    def update_borrowed_book(self, id, customer_id, book_id, start_date, end_date):
        self.cursor.execute("UPDATE borrowed_books SET customer_id=?, book_id=?, start_date=?, end_date=? WHERE id=?", (customer_id, book_id, start_date, end_date, id))
        self.db.commit()

    def delete_borrowed_book(self, id):
        self.cursor.execute("DELETE FROM borrowed_books WHERE id=?", (id,))
        self.db.commit()

    def get_all_borrowed_books(self):
        self.cursor.execute("SELECT * FROM borrowed_books")
        return self.cursor.fetchall()

    def get_borrowed_book(self, id):
        self.cursor.execute("SELECT * FROM borrowed_books WHERE id=?", (id,))
        return self.cursor.fetchone()
    
class usersDbhandler(Datenbank):
    def __init__(self):
        super().__init__()

    def add_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
        self.db.commit()

    def update_user(self, id, username, password):
        self.cursor.execute("UPDATE users SET username=?, password=? WHERE id=?", (username, password, id))
        self.db.commit()

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
        self.db.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        return self.cursor.fetchone()