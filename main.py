'''
Обязательные пункты меню:
1 Просмотр записей
2 Добавление записи
3 Экспорт (не менее двух форматов)
4 Импорт (не менее двух форматов)
5 Выход из программы (программа должна работать, пока пользователь сам не выйдет из неё)

'''


import viewer
import add
import importation
import checker
import export
import logger


def main_menu():
    print('Выберите действие: ')
    print('Нажмите 1 для просмотра записей.')
    print('Нажмите 2 для добавления записи')
    print('Нажмите 3 для экспорта файла.')
    print('Нажмите 4 для импорта файла.')
    print('Нажмите 5 для выхода из программы.')
    choice = input('Ваш выбор: ')
    choice = checker.check_choice(choice)
    logger.log('Выбор в главном меню', choice)
    if choice == 1:
        print('Для просмотра записей в формате\n\
                <Фамилия>\n\
                <Имя>\n\
                <Телефон>\n\
                <Описание>\n\
                нажмите 1')
        print('Для просмотра записей в формате\n\
                <Фамилия>, <Имя>, <Телефон>, <Описание>\n\
                нажмите 2')
        choice1 = input()
        choice1 = checker.check_choice_in_add(choice1)
        logger.log('Выбор формата просмотра записи', choice1)
        if choice1 == 1:
            viewer.view_notes2()
        if choice1 == 2:
            viewer.view_notes()
        main_menu()
    if choice == 2:
        logger.log('Добавление новой записи')
        add.add_note()
        main_menu()
    if choice == 3:
        print('Для экспорта записей в формате\n\
                <Фамилия>\n\
                <Имя>\n\
                <Телефон>\n\
                <Описание>\n\
                нажмите 1')
        print('Для экспорта записей в формате\n\
                <Фамилия>, <Имя>, <Телефон>, <Описание>\n\
                нажмите 2')
        choice3 = input()
        choice3 = checker.check_choice_in_add(choice3)
        logger.log('Выбор формата экспорта записей', choice3)
        if choice3 == 1:
            export.export_file2()
        if choice3 == 2:
            export.export_file()
        main_menu()
    if choice == 4:
        print('Для импорта записей в формате\n\
                <Фамилия>\n\
                <Имя>\n\
                <Телефон>\n\
                <Описание>\n\
                нажмите 1')
        print('Для импорта записей в формате\n\
                <Фамилия>, <Имя>, <Телефон>, <Описание>\n\
                нажмите 2')
        choice4 = input()
        choice4 = checker.check_choice_in_add(choice4)
        logger.log('Выбор формата импорта записей', choice4)
        if choice4 == 1:
            importation.import_file()
        if choice4 == 2:
            importation.import_file2()
        main_menu()
    if choice == 5:
        return print('Всего хорошего!')


main_menu()
