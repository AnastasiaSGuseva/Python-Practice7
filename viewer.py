import logger


def view_notes():
    with open('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all_list = note_for_read.read().split('\n')
        if '' in all_list:
            all_list.remove('')
        if '    ' in all_list:
            all_list.remove('    ')
        for i in range(len(all_list)):
            print(', '.join(all_list[i].split()))
    
    logger.log('Просмотр записей в формате 2')


def view_notes2():
    with open('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all_list = note_for_read.read().split('\n')
        if '' in all_list:
            all_list.remove('')
        if '    ' in all_list:
            all_list.remove('    ')
        for i in range(len(all_list)):
            print('\n'.join(all_list[i].split()), end='')
            print('\n')

    logger.log('Просмотр записей в формате 1')
