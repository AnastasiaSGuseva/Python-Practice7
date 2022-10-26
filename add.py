import checker
import logger

def add_note():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    description = input('Введите описание: ')
    list1 = [surname, name, number, description]
    logger.log('Добавление записи', list1)


    with open ('note_file.txt', 'a', encoding='UTF-8') as note_file:
        for item in list1:
            note_file.write(item)
            note_file.write(' ')
        note_file.write('\n')

    print('Для добавления следующей записи нажмите 1.')
    print('Для выхода в главное меню нажмите 2.')
    choise = input()
    choise = checker.check_choise_in_add(choise)
    if choise == 1:
        add_note()
    else:
        return
