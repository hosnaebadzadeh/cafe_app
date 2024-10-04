import sqlite3


conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_name TEXT NOT NULL,
    price REAL NOT NULL,
    amount INTEGER NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    price REAL ,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ,
    UNIQUE(customer_id)
)
''')


conn.commit()
conn.close()