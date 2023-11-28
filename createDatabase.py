import sqlite3

# Specify the path and name of the database file
database_path = 'Database.db'

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect(database_path)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table for books
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    publication_year INTEGER,
                    description TEXT,
                    ESBN TEXT,
                    genre TEXT,
                    language TEXT,
                    publisher TEXT,
                    pages INTEGER,
                    borrowed BOOLEAN
                )''')

# Create a table for users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT
                )''')

# Create a table for borrowed books
cursor.execute('''CREATE TABLE IF NOT EXISTS borrowed_books (
                    id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    book_id INTEGER,
                    start_date TEXT,
                    end_date TEXT,
                    FOREIGN KEY(customer_id) REFERENCES customer(id),
                    FOREIGN KEY(book_id) REFERENCES books(id)
                )''')

# Create a table for Customer
cursor.execute('''CREATE TABLE IF NOT EXISTS customer (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    address TEXT,
                    phone TEXT,
                    email TEXT,
                    username TEXT,
                    password TEXT,
                    Age INTEGER
                )''')


cursor.execute(''' 
            INSERT INTO users (username, password) VALUES ('admin', 'admin')
                ''')    

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
