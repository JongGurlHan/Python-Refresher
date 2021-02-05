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