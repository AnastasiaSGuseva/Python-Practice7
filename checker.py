def check_choice(ch):
    while not ch.isdigit():
        ch = input('Введите число: ')
    else:
        while int(ch) < 1 or int(ch) > 5:
            ch = input('Введите целое число от 1 до 5: ')
        else:
            return int(ch)


def check_choice_in_add(ch):
    while not ch.isdigit():
        ch = input('Введите число: ')
    else:
        while int(ch) < 1 or int(ch) > 2:
            ch = input('Введите целое число от 1 до 2: ')
        else:
            return int(ch)
