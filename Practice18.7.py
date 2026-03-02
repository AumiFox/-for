import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить имя нового ученика
        5. Редактировать имя ученика
        6. Удалить имя ученика
        7. Добавить новый предмет
        8. Редактировать название предмета
        9. Удалить предмет
        10. Редактировать оценку ученика по предмету
        11. Удалить оценку ученика по предмету
        12. Вывести информацию по всем оценкам по ученику
        13. Вывести средний балл по каждому предмету по ученику
        14. Средний балл класса по каждому предмету
        15. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Добавить имя нового ученика')
        new_student = input('Введите имя ученика: ')
        students.append(new_student)
        students.sort()
        students_marks[new_student] = {}
        for class_ in classes:
            students_marks[new_student][class_] = []
        if new_student not in students:
            print('Ученик добавлен')
        else:
            print('Такой ученик уже есть')
    elif command == 5:
        print('5. Редактировать имя ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            new_student = input('Введите новое имя ученика: ')
            if new_student not in students:
                index = students.index(student)
                students[index] = new_student
                students.sort()
                students_marks[new_student] = students_marks.pop(student)
                print('Имя успешно отредактировано')
            else:
                print('Ученик с таким именем уже существует')
        else:
            print('Такого имени нет')
    elif command == 6:
        print('6. Удалить имя ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            students.remove(student)
            del students_marks[student]
            print('Имя успешно удалено')
        else:
            print('Такого имени нет')
    elif command == 7:
        print('7. Добавить новый предмет')
        new_class = input('Введите название нового предмета: ')
        classes.append(new_class)
        if new_class not in classes:
            classes.sort()
            for student in students_marks:
                students_marks[student][new_class] = []
            print('Предмет добавлен')
        else:
            print('Такой предмет уже есть')
    elif command == 8:
        print('8. Редактировать название предмета')
        class_ = input('Введите название предмета: ')
        if class_ in classes:
            new_class = input('Введите новое название предмета: ')
            if new_class not in classes:
                index = classes.index(class_)
                classes[index] = new_class
                classes.sort()
                for student in students_marks:
                    students_marks[student][new_class] = students_marks[student].pop(class_)
                print('Название предмета успешно отредактировано')
            else:
                print('Предмет с таким названием уже существует')
        else:
            print('Такого предмета нет')
    elif command == 9:
        print('9. Удалить предмет')
        class_ = input('Введите имя ученика: ')
        if class_ in classes:
            students.remove(class_)
            for student in students_marks:
                del students_marks[student][class_]
            print('Предмет успешно удалено')
        else:
            print('Такого предмета нет')
    elif command == 10:
        print('10. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f'Текущие оценки: {students_marks[student][class_]}')
            mark_index = int(input('Введите номер оценки для редактирования (начиная с 0): '))
            if 0 <= mark_index < len(students_marks[student][class_]):
                new_mark = int(input('Введите новую оценку: '))
                old_mark = students_marks[student][class_][mark_index]
                students_marks[student][class_][mark_index] = new_mark
                print(f'Оценка {old_mark} изменена на {new_mark}')
            else:
                print('ОШИБКА: неверный номер оценки')
        else:
            print('Ошибка в имени ученика или в предмете')
    elif command == 11:
        print('11. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите название предмета: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(f'Текущие оценки: {students_marks[student][class_]}')
            mark_index = int(input('Введите номер оценки для удаления (начиная с 0): '))
            if 0 <= mark_index < len(students_marks[student][class_]):
                removed_mark = students_marks[student][class_].pop(mark_index)
                print(f'Удалена оценка {removed_mark}')
            else:
                print('ОШИБКА: неверный номер оценки')
        else:
            print('Ошибка в имени ученика или в предмете')
    elif command == 12:
        print('12. Вывести информацию по всем оценкам по ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'\nОценки ученика {student}:')
            for class_ in classes:
                if class_ in students_marks[student]:
                    print(f'  {class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: ученик не найден')
    elif command == 13:
        print('13. Вывести средний балл по каждому предмету по ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'\nСредний балл для ученика {student}:')
            for class_ in classes:
                if class_ in students_marks[student]:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    average = marks_sum / marks_count
                    print(f'  {class_} - {average:.2f}')
        else:
            print('ОШИБКА: ученик не найден')
    elif command == 14:
         print('14. Средний балл класса по каждому предмету')
         print('=' * 40)
         for class_ in classes:
                total_sum = 0
                total_count = 0
                for student in students:
                    if class_ in students_marks[student]:
                        total_sum += sum(students_marks[student][class_])
                        total_count += len(students_marks[student][class_])
                if total_count > 0:
                    average = total_sum / total_count
                    print(f'{class_}: {average:.2f}')
                else:
                    print(f'{class_}: нет оценок')
    elif command == 15:
        print('15. Выход из программы')
        break
