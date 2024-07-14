class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} returned.")
        else:
            print(f"{self.title} is already available.")

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found.")

    def list_available_books(self):
        print("Available Books:")
        for book in self._books:
            if not book._is_checked_out:
                print(f"- {book.title} by {book.author}")