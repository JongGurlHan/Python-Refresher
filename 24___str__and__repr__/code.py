class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # def __str__(self): #turn the object into a string using the str method
    #     return f"Person {self.name}, {self.age} years old"

    def __repr__(self): # if possible, it should return a string that allows us to recreate the original object very easily
        return f"<Person('{self.name}', {self.age})>"

bob  = Person("Bob", 35)
print(bob) 

#__str__ method: turn object into a string 
#__repr__ method: used to print out an unambiguous representation of an object so that you can use that to recreate the object for example
