import pytest
from lib.models.author import Author
from lib.db.connection import get_connection

def test_create_author():
    author = Author(name="John Doe")
    author.save()
    assert author.id is not None

def test_find_author_by_id():
    author = Author(name="Jane Doe")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Jane Doe"

def test_find_author_by_name():
    author = Author(name="Alice Smith")
    author.save()
    found = Author.find_by_name("Alice Smith")
    assert found.id == author.id
