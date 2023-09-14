def filter_students_by_grade(students):
    # TODO: Nutze eine List Comprehension, um Studenten zu filtern, deren Note kleiner als 4.0 ist.
    return [student for student in students if student[1] < 4.0]
    # oder: return [(name, grade) for name, grade in students if grade < 4.0]

if __name__ == '__main__':
    students = [
        ('Alice', 4.0),
        ('Bob', 3.5),
        ('Charlie', 4.25),
        ('David', 5.5),
        ('Manuel', 3.75)
    ]
    result = filter_students_by_grade(students)
    print(result)
