student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequece):
    return sum(sequece) / len(sequece)


print(average(student["grades"]))