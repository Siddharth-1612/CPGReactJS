class Book:
    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        new_series = BookSeries()
        new_series.add_book(self.title)
        new_series.add_book(other.title) 
        return new_series

class BookSeries:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)  

    def display(self):
        print("Books in the series:", ", ".join(self.books))

book_1 = Book("Harry Potter")
book_2 = Book("The Lord of the Rings")

books = book_1 + book_2

books.display()
