from lib.models.author import Author
from lib.models.magazine import Magazine

if __name__ == "__main__":
    author = Author("Alice")
    author.save()

    mag = Magazine("Tech Times", "Technology")
    mag.save()

    author.add_article(mag, "AI in 2025")

    for a in author.articles():
        print("Article:", a.title)

    for m in author.magazines():
        print("Magazine:", m.name)

    print("Categories:", author.topic_areas())
