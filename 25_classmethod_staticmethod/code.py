class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): #doesn't have parameter This really isn't a method, It's just a function that you've placed inside a clas
        print("Called static_method.")

test = ClassTest()
test.instance_method()
print("================================================")
ClassTest.class_method()
print("================================================")
ClassTest.static_method()

#instance methods are used for most things. W
#When you wanna produce an action that uses the data inside the object that you created earlier on for example,
#that is when instance methos would get used 
#Also if you wanna call a method to modify some sort of data inside self or the object, then you would also use an instance method. 

#Class methods are used often as factories 

#static methods are used to just place a method inside a class. Because you feel like it belongs there for some reason 
#for you as a developer, you wanna put that method in there because it makes sense logically for code organisation or sth like that  