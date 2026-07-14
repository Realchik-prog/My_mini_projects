from random import choice
rules = input('Нужно рассказывать правила? (да): ').lower() == 'да'
if rules:
    print()
    print('Правила: ')
    print('Программа загадывает многозначное число. Ваша задача - отгадать его, вводя числа такой же длины цифр.')
    print('Программа будет говорить вам, какие по счёту цифры в вашем числе совпали с загаданным числом и какие стоят не на своём месте')
    print('Удачи!')
print()
while True:
    try:
        digits = int(input('Сколько будет цифр в числе?: '))
        if digits>1:
            break
        else:
            print('Цифр должно быть больше одной')
    except ValueError:
        print('Не число!')

number = ''.join([str(choice(range(0, 10))) for _ in range(digits)])
attempts_count = 0
right_count_list = []
see = False
while True:
    while True:
        try:
            attempt = input('Введите предполагаемое число: ')
            if attempt.lower() == 'показать':
                print(number)
                see = True
                break
            elif int(attempt)==int(attempt) and len(attempt)!=digits:
                print('Неверное количество цифр')
            else:
                break
        except ValueError:
            print('Не число!')
    if attempt.lower() != 'показать':
        attempts_count += 1
        if attempt == number:
            print('Вы разгадали число. Поздравляю с победой!')
            right_count_list.append((digits, 0))
            break
        else:
            green_count = 0
            yellow_count = 0
            count_book = {}
            for digit in number:
                count_book[digit] = 0
            green = set()
            not_first = True
            for index, digit in enumerate(number):
                if digit == attempt[index]:
                    green_count += 1
                    if not_first:
                        print(f'Совпали цифры по счёту: {index+1}', end='')
                        not_first = False
                    else:
                        print(f', {index+1}', end='')
                    count_book[digit] += 1
                    if count_book[digit] == number.count(digit):
                        green.add(digit)
            if not_first:
                print('Никакие цифры не совпали', end='')
            print()
            not_first = True
            for index, digit in enumerate(attempt):
                if digit in number and digit not in green and digit != number[index]:
                    yellow_count += 1
                    if not_first:
                        print(f'Цифры не на своих местах по счёту: {index + 1}', end='')
                        not_first = False
                    else:
                        print(f', {index + 1}', end='')
                    count_book[digit] += 1
                    if count_book[digit] == number.count(digit):
                        green.add(digit)
            print()
            if not_first:
                print('Никакие цифры не стоят не на своих местах', end='')
            print()
            right_count_list.append((green_count, yellow_count))

print()
print('СТАТИСТИКА')
print(f'Сделано попыток: {attempts_count}')
print(f'Количество угаданных цифр в каждой попытке: {right_count_list} (на своём месте, не на своём)')
print(f'Число показано: {'да' if see else 'нет'}')