import logger

def view_notes():
    with open ('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all = note_for_read.read().split('\n')
        if '' in all:
            all.remove('')
        if '    ' in all:
            all.remove('    ')
        for i in range(len(all)):
            print(', '.join(all[i].split()))
    
    logger.log('Просмотр записей в формате 2')


def view_notes2():
    with open ('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all = note_for_read.read().split('\n')
        if '' in all:
            all.remove('')
        if '    ' in all:
            all.remove('    ')
        for i in range(len(all)):
            print('\n'.join(all[i].split()), end='')
            print('\n')

    logger.log('Просмотр записей в формате 1')
