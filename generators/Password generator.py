from random import randint, random
while True:
    # Ввод возможных символов
    a = input('Какие символы будут в пароле?(1 - цифры, 2 - рус. буквы, 3 - англ. буквы, 4 - специальные символы): ')
    m = set()
    if '1' in a:
        m = m | {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    if '2' in a:
        m = m | set(list('ёйцукенгшщзхъфывапролджэячсмитьбю'))
    if '3' in a:
        m = m | set(list('qwertyuiopasdfghjklzxcvbnm'))
    if '4' in a:
        m = m | set(list('~!@"#№$;%:^&?*()-_=+\\/|{}[]<>'))
    if m == set():
        print('Неправильный ввод')
    else:
        break
if "2" in a or "3" in a:
    while True:
        # Ввод регистра
        lower_and_upper = input('Регистр (верхний, нижний, любой): ')
        if lower_and_upper.lower() == 'верхний' or lower_and_upper.lower() == 'нижний' or lower_and_upper.lower() == 'любой':
            break
        else:
            print('Неправильный ввод')
while True:
    try:
        count = int(input('Сколько символов будет в пароле?: '))
        break
    except ValueError:
        print('Неправильный ввод')
password = ''
for _ in range(count):
    char = list(m)[randint(0, len(m)-1)]
    if {char} & set(list('ёйцукенгшщзхъфывапролджэячсмитьбюqwertyuiopasdfghjklzxcvbnm')) != set():
        if lower_and_upper.lower() == 'любой':
            if random()<0.5:
                char = char.upper()
        elif lower_and_upper.lower() == 'верхний':
            char = char.upper()
    password += char
print(password)