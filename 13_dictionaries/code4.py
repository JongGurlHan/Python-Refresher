student_attendance = {"Rolf":96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items))
attendance_values = student_attendance.values()

print(sum(attendance_values) / len(attendance_values))