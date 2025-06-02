import os
import sqlite3

DB_FILE = "data/finance.db"

# Automatically create the directory if needed
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    # Example table creation (modify as needed)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


