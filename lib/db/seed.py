import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


# lib/db/seed.py

from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert Authors
    cursor.execute("INSERT INTO authors (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Bob')")
    cursor.execute("INSERT INTO authors (name) VALUES ('Charlie')")

    # Insert Magazines
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Today', 'Technology')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Health Weekly', 'Health')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Travel Now', 'Travel')")

    # Insert Articles
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Fitness 101', 2, 2)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Exploring Europe', 1, 3)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Tech for Good', 3, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Healthy Living', 1, 2)")

    conn.commit()
    conn.close()
    print("Database seeded.")

if __name__ == "__main__":
    seed_data()
