class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # @classmethod
    # def hardcover(cls, name, page_weight):
    #     return Book(name, Book.TYPES[0], page_weight +100)

    # @classmethod
    # def paperback(cls, name, page_weight):
    #     return Book(name, Book.TYPES[1], page_weight)
   
    @classmethod
    def hardcover(cls, name, page_weight): #Because you have access at the class ifself inside the method, that means that it is a perfect place to be creating new objects by using that class
        return cls(name, cls.TYPES[0], page_weight +100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
    
print("=================================================")

newBook = Book("little prince", "novel", 100)

print(newBook.name)
print(newBook) 

print("=================================================")

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)
print(light)