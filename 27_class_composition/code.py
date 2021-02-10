#composition allows your classes to be simpler and reduces teh complexity of your code overall 

class BookShelf:
    # def __init__(self, quantity):
    #     self.quantity = quantity

    # def __str__(self):
    #     return f"BookShelf with {self.quantity} books."
    def __init__(self, *books):     
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

shelf = BookShelf(300) 

class Book():
    # def __init__(self, name, quantity):
    #     super().__init__(quantity)
    #     self.name = name
    
    def __init__(self, name):        
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

# book  = Book("Harry Potter", 120)
# print(book)

#This is a bad appraoch for 2 reasons
#1. conceptual reason: when you do inheritance, you're essentially treating like evolutionary inheritance
#You're saying that a book is a bookshelf and sth more. 
#2. Technical reason: You've got this book class that inherits from bookshelf, 
# but actually you are not using inside it anything about the bookshelf. So you are completely overriding the str method

#Instead of setting the quantity of books in the bookself, we're actually going to allow constructor to take in a number of books

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
print(shelf.books)