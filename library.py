class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"{book_name} added successfully.")
         def view_books(self):
        print(self.books)