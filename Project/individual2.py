#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from package import *


get_student = get.get_student
display_students = display.display_students
select_students = select.select_students


def main():
    """
    Главная функция программы.
    """
    # Список студентов.
    students = []

    # бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            student = get_student()

            # Добавить словарь в список.
            students.append(student)
            # Сортировка по возрастанию среднего балла
            students.sort(key=lambda x: sum(x['grades']) / 5)

        elif command == 'list':
            # Отобразить всех студентов.
            display_students(students)

        elif command == 'select':
            selected = select_students(students)
            # Отобразить выбранных студентов.
            display_students(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select - запросить студентов, имеющих оценки 4, 5;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
