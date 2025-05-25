class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("Aangan", "Khadija Mastoor")
book2 = Book("My Feudal Lord", "Tehmina Durrani")
book3 = Book("Ghulam Bagh", "Mirza Athar Baig")

print("Total books:", Book.total_books)
