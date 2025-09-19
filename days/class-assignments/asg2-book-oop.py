from collections import defaultdict

class Book:
    def __init__(self, book_ID, title, author, status, issue_date):
        self.book_ID, self.title, self.author, self.status, self.issue_date = book_ID, title, author, status, issue_date


class Member:
    def __init__(self, member_ID, name, issued_books):
        self.member_ID, self.name, self.issued_books = member_ID, name, issued_books

    def list_of_books(self):
        Library.get_member_books(self.member_ID)

class Library:
    books_list = []
    member_issued_books = defaultdict(list)
    def __init__(self):
        self.books_list = self.books_list
        self.member_issued_books = Library.member_issued_books

    def add_book(self, book):
        self.books_list.append(book)

    def display_books(self):
        for book in self.books_list:
            print(f'Book : ID = {book.book_ID}, title = {book.title}, author = {book.author}, status = {book.status}, issue date = {book.issue_date}')


    def issue_book(self, member_ID, book_ID):
        for book in self.books_list:
            if book_ID == book.book_ID and book.status == 'Available':
                self.member_issued_books[member_ID].append(book_ID)
                book.status = 'Issued'
                break
        else:
            print("Book is not available")

    def return_book(self, book_ID):
        for book in self.books_list:
            if book.book_ID == book_ID and book.status == 'Issued':
                book.status = 'Available'
        else:
            print("Book is not available")

    @staticmethod
    def get_member_books( member_ID):
        l = []
        for key in Library.member_issued_books:
            if key == member_ID:
                l.append(Library.member_issued_books[key])
        print("Books issued by you: ", l[0])




b1 = Book(1,"Book1","Chirang", "Available", '2025-05-01')
b2 = Book(2,"Book2","Agrinma", "Issued",'2025-05-01')
b3 = Book(3,"Book3","Aman", "Issued",'2025-05-01')
b4 = Book(4,"Book4","Pankaj", "Available",'2025-05-01')
library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
library.display_books()

m1 = Member(101,"Gaga", None)
library.issue_book(101,1)
library.issue_book(101,2)
library.issue_book(101,3)
library.issue_book(101,4)
m1.list_of_books()
