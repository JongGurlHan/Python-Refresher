# t= 5,11
# x,y = t
# print(x,y)

student_attendance = {"Rolf":96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(student)
    # print(f"{student} : {attendance}")