from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(f"{author.id}. {author.name}")

def list_magazines():
    magazines = Magazine.get_all()
    for mag in magazines:
        print(f"{mag.id}. {mag.name} ({mag.category})")

def list_articles():
    articles = Article.get_all()
    for art in articles:
        print(f"{art.id}. {art.title}")

def menu():
    while True:
        print("\nMenu:")
        print("1. List authors")
        print("2. List magazines")
        print("3. List articles")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            list_authors()
        elif choice == "2":
            list_magazines()
        elif choice == "3":
            list_articles()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
