class Student:
    def  __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 79, 88, 95))
student2 = Student("Rolf", (100, 79, 88, 95))
print(student.name)
print(student.grades)
print(student.average())
print(student2.average()) 