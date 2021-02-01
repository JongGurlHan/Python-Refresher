people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"),("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"name:{name}, age:{age}, profession:{profession}")

for person in people:
    print(f"Name:{person[0]} ,Age :{person[1]}, Profession :{person[2]}")