from collections import defaultdict
from datetime import time, date


class Book:
    def __init__(self, name ,category, price, author, currentOwner, printingDate):
        self.name = name
        self.category = category
        self.price = price
        self.author = author
        self.currentOwner = currentOwner
        self.printingDate = printingDate

class Category:
    def __init__(self, name):
        self.name = name
        self.books = defaultdict(list)
    def addBook(self, name, book):
        self.books[name].append(book)
    def delBook(self, name):
        if name in self.books and len(self.books) > 0:
            self.books.pop()
    def getBook(self, name):
        for book in self.books[name]:

            return book

class Account:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.creationDate = date.today()

class Customer(Account):
    def __init__(self, name, id, bill, lastBookTaken, lastBookTakenDate):
        super().__init__(name, id)
        self.bill = bill
        self.lastBookTaken = lastBookTaken
        self.lastBookTakenDate = lastBookTakenDate

class Library:
    def __init__(self, id, rate):
        self.category = defaultdict(Category)
        self.booksCategory = defaultdict(str)
        self.id = id
        self.customerAccount = defaultdict(Customer)
        self.rate = rate

    def add_book(self, name ,category, price, author, currentOwner, printingDate):
        newBook = Book(name ,category, price, author, currentOwner, printingDate)
        if category not in self.category:
            self.category[category] = Category(category)
        self.category[category].addBook(name, newBook)
        if name not in self.booksCategory:
            self.booksCategory[name] = category
    def del_book(self, name):
        category = self.booksCategory[name]
        if category:
            return self.category[category].delBook(name)
        else:
            return -1
    def getCategory(self, name):
        if name in self.booksCategory:
            return self.booksCategory[name]
        else:
            return -1
    def issue_Book(self, name, ownerID):
        category = self.getCategory(name)
        if category:
            book  = self.category[category].getBook(name)
            if not book:
                print('Book Not Found. Sorry')
                return -1
            else:
                book.currentOwner = ownerID
                self.customerAccount[ownerID].lastBookTaken = name
                self.customerAccount[ownerID].lastBookTakenDate = date.today()
                print('Book Issued')
    def returnBook(self, name, ownerID):
        category = self.getCategory(name)

        if category:
            book  = self.category[category].getBook(name)

            book.currentOwner = None
            self.customerAccount[ownerID].lastBookTaken = None
            self.customerAccount[ownerID].lastBookTakenDate = None
    def calculateBill(self, name):
        self.customerAccount[name].bill = (date.today() - self.customerAccount[name].creationDate) * self.rate
        return self.customerAccount[name].bill
    def add_account(self, customer):
        self.customerAccount[customer.id] = customer







library = Library(1, 15)
customer = Customer('Pauravi',1, 0, None, None)
library.add_account(customer)
library.add_book('Harry Potter', 'Fiction', 250, 'JK', None, None)
library.issue_Book('Harry Potter', 1)
library.returnBook('Harry Potter', 1)



