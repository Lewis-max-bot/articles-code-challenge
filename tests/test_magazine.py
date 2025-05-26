import pytest
from lib.models.magazine import Magazine

def test_create_magazine():
    mag = Magazine(name="Tech Today", category="Technology")
    mag.save()
    assert mag.id is not None

def test_find_magazine_by_name():
    mag = Magazine(name="Nature Now", category="Science")
    mag.save()
    found = Magazine.find_by_name("Nature Now")
    assert found.id == mag.id

def test_find_magazine_by_category():
    mag = Magazine(name="Food Fun", category="Cooking")
    mag.save()
    mags = Magazine.find_by_category("Cooking")
    assert any(m.name == "Food Fun" for m in mags)
