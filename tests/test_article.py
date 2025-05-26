import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_create_article():
    author = Author(name="Tim Writer")
    author.save()
    magazine = Magazine(name="Health Weekly", category="Health")
    magazine.save()
    article = Article(title="Benefits of Running", author_id=author.id, magazine_id=magazine.id)
    article.save()
    assert article.id is not None

def test_find_article_by_title():
    author = Author(name="Sara Article")
    author.save()
    magazine = Magazine(name="Science Daily", category="Science")
    magazine.save()
    article = Article(title="Black Holes", author_id=author.id, magazine_id=magazine.id)
    article.save()
    found = Article.find_by_title("Black Holes")
    assert found.title == "Black Holes"
