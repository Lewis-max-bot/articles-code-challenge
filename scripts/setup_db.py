# scripts/setup_db.py

import sqlite3

def setup_db():
    connection = sqlite3.connect("articles.db")
    cursor = connection.cursor()

    with open("lib/db/schema.sql") as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_db()

