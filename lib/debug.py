import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    print("Welcome to the interactive debug console!\n")

    # List all authors
    print("All authors:")
    for author_id in range(1, 4):
        author = Author.find_by_id(author_id)
        print(f"Author {author.id}: {author.name}")
        print(f"  Articles: {[article.title for article in author.articles()]}")
        print(f"  Magazines: {[mag.name for mag in author.magazines()]}")
        print(f"  Topic Areas: {author.topic_areas()}")
        print()

    # Example: Create a new article for author 1
    alice = Author.find_by_id(1)
    tech_today = Magazine.find_by_id(1)
    new_article = alice.add_article(tech_today, "The Future of Robotics")
    print(f"Added new article: {new_article.title} by {alice.name} in {tech_today.name}")

if __name__ == "__main__":
    main()
