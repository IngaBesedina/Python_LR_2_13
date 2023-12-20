def select_students(staff):
    # Сформировать список студентов, имеющих оценки 4 и 5.
    result = []
    for student in staff:
        if all(grade >= 4 for grade in student['grades']):
            result.append(student)

    # Возвратить список выбранных студентов.
    return result
