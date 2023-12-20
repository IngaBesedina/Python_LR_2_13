def get_student():
    """
    Запросить данные о студенте.
    """
    surname = input("Введите фамилию и инициалы: ")
    group_num = input("Введите номер группы: ")
    print('Введите оценки: ')
    grades = [int(n) for n in input().split()]

    student = {
        'name': surname,
        'group_number': group_num,
        'grades': grades
    }

    return student
