students = [
    {"name": "Ali", "age": 20},
    {"name": "Dana", "age": 18},
    {"name": "Murat", "age": 22}
]

sorted_students = sorted(students, key=lambda x: x["age"])

print(sorted_students)