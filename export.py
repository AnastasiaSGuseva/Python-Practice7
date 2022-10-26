import logger

def export_file():
    with open ('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all = note_for_read.read().split('\n')
        if '' in all:
            all.remove('')
        if '    ' in all:
            all.remove('    ')

    path = input('Укажите путь и имя сохранения файла в формате C:\...\item_name.txt: ')
    with open (path, 'a', encoding='UTF-8') as note_for_write:
        for i in range(len(all)):
            note_for_write.write(', '.join(all[i].split()))
            note_for_write.write('\n')
    logger.log('Экспорт файла в формате 2', path)  

def export_file2():
    with open ('note_file.txt', 'r', encoding='UTF-8') as note_for_read:
        all = note_for_read.read().split('\n')
        if '' in all:
            all.remove('')
        if '    ' in all:
            all.remove('    ')

    path = input('Укажите путь и имя сохранения файла в формате C:\...\item_name.txt: ')
    with open (path, 'a', encoding='UTF-8') as note_for_write:
        for i in range(len(all)):
            note_for_write.write('\n'.join(all[i].split()))
            note_for_write.write('\n\n')
    logger.log('Экспорт файла в формате 1', path)