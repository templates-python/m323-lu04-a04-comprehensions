def filter_students_by_grade(students):
    """
    Nutze eine List Comprehension, um Studenten zu filtern, deren Note kleiner als 4.0 ist.

    Parameters:
    - students (list): Liste der Studenten und ihrer Noten.

    Returns:
    - list: Liste der gefilterten Studenten.
    """
    return []


if __name__ == '__main__':
    students = [
        ('Alice', 4.0),
        ('Bob', 3.5),
        ('Charlie', 4.25),
        ('David', 5.5),
        ('Manuel', 3.75),
    ]
    result = filter_students_by_grade(students)
    print(result)
