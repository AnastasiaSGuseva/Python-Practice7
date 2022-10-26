import logger

def import_file():
    path = input('Укажите путь и имя файла в формате C:\...\file_name.txt: ')

    with open (path, 'r', encoding='UTF-8') as imp_file:
        all_imp = imp_file.read()
        all = all_imp.split('\n')
        i = 0
        while i in range(len(all)):
            if all[i] == '':
                all.remove('')
            if all[i] == '    ':
                all.remove('    ')
            i = i + 1
        if '' in all:
            all.remove('')
        if '    ' in all:
            all.remove('    ')
        all1 = []
        i = 0
        while i < len(all):
            all1.append(all[i])
            all1.append(all[i+1])
            all1.append(all[i+2])
            all1.append(all[i+3])
            all1.append('\n')
            i = i + 4

        with open('note_file.txt', 'a', encoding='UTF-8') as note_file:
            note_file.write(' '.join(all1))
    
    logger.log('Импорт файла в формате 1', path)

def import_file2():
    path = input('Укажите путь и имя файла в формате C:\...\file_name.txt: ')

    with open (path, 'r', encoding='UTF-8') as imp_file:
        all = imp_file.read().split('\n')
        for i in range(len(all)):
            all[i] = all[i].replace(', ', ' ')
        all.remove('')

    with open('note_file.txt', 'a', encoding='UTF-8') as note_file:
            note_file.write('\n'.join(all))
            note_file.write('\n')
    
    logger.log('Импорт файла в формате 2', path)

