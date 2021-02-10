def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannnot be 0")
    return dividend / divisor

students = [
    {"name":"Bob", "grades": [30,55]},
    {"name":"James", "grades": []},
    {"name":"Katty", "grades": [40,65]},
]

try:
    for student in students:
        name = student["name"]
        grade = student["grades"]
        average = devide(sum(grade), len(grade))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    print(f"Error: {name} has no grades")
else:
    print("--All student averages calculated--")
finally:
    print("--End of student average calculation--")