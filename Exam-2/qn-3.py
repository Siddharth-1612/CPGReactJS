class book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"tne title of the book is {self.title}")
        print(f"the author of the book is {self.author}")
        print(f"the ISBN number of the book is {self.isbn}")
title=input("enter the Title of the book: ")
author=input("enter the name of the author: ")
isbn=input("enter the ISBN number of the book: ")
book_details=book(title,author,isbn)
book_details.display()