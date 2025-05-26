import sys
import os

# Add the root folder to the Python path so we can import lib.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.schema import create_tables

if __name__ == "__main__":
    create_tables()
    print("Database setup complete!")
