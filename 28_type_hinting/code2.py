class Book:
    def __init__(self, name:str, page_count: int):
        self.name = name
        self.page_count = page_count

    def __str__(self):
        return f"{self.name} {self.page_count}"


book1 = Book(12, "harry")
print(book1)