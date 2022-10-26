import datetime

def log(text = 'действие', value = None,):
    if value == None:
        value = ''
    # if text == None:
    #     text = ''
    date = datetime.datetime.now().strftime('%d-%m-%Y  %H:%M:%S')    

    with open('log.txt', 'a', encoding='UTF-8') as log:       
        log.write(f'{date} {text} {value} \n')
