import logger


def import_file():
    path = input('Укажите путь и имя файла в формате C:\...\file_name.txt: ')

    with open(path, 'r', encoding='UTF-8') as imp_file:
        all_imp = imp_file.read()
        all_list = all_imp.split('\n')
        i = 0
        while i in range(len(all_list)):
            if all_list[i] == '':
                all_list.remove('')
            if all_list[i] == '    ':
                all_list.remove('    ')
            i = i + 1
        if '' in all_list:
            all_list.remove('')
        if '    ' in all_list:
            all_list.remove('    ')
        all1 = []
        i = 0
        while i < len(all_list):
            all1.append(all_list[i])
            all1.append(all_list[i+1])
            all1.append(all_list[i+2])
            all1.append(all_list[i+3])
            all1.append('\n')
            i = i + 4

        with open('note_file.txt', 'a', encoding='UTF-8') as note_file:
            note_file.write(' '.join(all1))
    
    logger.log('Импорт файла в формате 1', path)


def import_file2():
    path = input('Укажите путь и имя файла в формате C:\...\file_name.txt: ')

    with open(path, 'r', encoding='UTF-8') as imp_file:
        all_list = imp_file.read().split('\n')
        for i in range(len(all_list)):
            all_list[i] = all_list[i].replace(', ', ' ')
        all_list.remove('')

    with open('note_file.txt', 'a', encoding='UTF-8') as note_file:
        note_file.write('\n'.join(all_list))
        note_file.write('\n')
    
    logger.log('Импорт файла в формате 2', path)
