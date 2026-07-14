designations= {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
               21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V',
               32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
def by_10():
    number_chek=False
    # Проверка вводимого десятичного числа на неотрицательность
    while not number_chek:
        a=int(input('Введите десятичное число: '))
        if a<0:
            print('Только неотрицательные числа!')
        else:
            number_chek=True
    b=a
    l=[]
    s_check=False
    # Проверка системы счисления
    while not s_check:
        s = int(input('Введите систему счисления, в которую хотите перевести: '))
        if s<2:
            print('Система счисления должна быть больше единицы!')
        else:
            s_check=True
    t=False # Переменная для осмотра, прошёл ли цикл хоть раз
    while b!=0:
        t=True
        # Посимвольный перевод числа
        c=b
        b=b//s
        l.append(c-b*s)
    if not t:
        l.append(0)
    if s>10:
        # Символы для систем счислений, больших 10
        for i in range(len(l)):
            if l[i] in designations:
                l[i]=designations[l[i]]
            elif l[i]>=36:
                l='Символы закончились'
                break
    # Вывод
    if l!='Символы закончились':
        print(f'{a} (10) = ', end='')
        for i in l[::-1]:
            print(i, end='')
        print(f' ({s})')
    else:
        print('Извините, но у нас закончились символы для такой большой системы счисления. Число вывести не получится')
def in_10():
    s_check=False
    while not s_check:
        s = int(input('Введите, из какой системы счисления переводить число: '))
        if s<2:
            print('Система счисления должна быть больше единицы!')
        else:
            s_check=True
    acceptable_numbers=[]
    if s<=10:
        for i in range(s):
            acceptable_numbers.append(i)
    if s>10:
        for i in range(10):
            acceptable_numbers.append(i)
        for i in range(10, s):
            acceptable_numbers.append(designations[i])
    print(f'Все цифры этой системы счисления: ', end='')
    for i in range(len(acceptable_numbers)-1):
        print(acceptable_numbers[i], end=', ')
    print(acceptable_numbers[len(acceptable_numbers)-1])
    number_chek = False
    while not number_chek:
        a=input(f'Введите число {s}-ой системы счисления: ')
        b=a
        if a[0]=='0':
            print('Число не может начинаться с нуля!')
            break
        a=list(a)
        for i, g in enumerate(a):
            digit_detected=False
            for j in range(s):
                if g == str(acceptable_numbers[j]):
                    a[i]=j
                    digit_detected=True
            if not digit_detected:
                print(a)
                a='Кажется вы неправильно записали число'
                break
        if a=='Кажется вы неправильно записали число':
            print(a)
        else:
            number_chek=True
            print('Число успешно преобразовано для понимания программой')
            l=0
            a=a[::-1]
            for i in range(len(a)):
                l+=a[i]*s**i
            print(f'{b} ({s}) = {l} (10)')
while True:
    print('Меню систем счисления:')
    print('1. Перевод из 10-ой системы в другую')
    print('2. Перевод из другой системы в 10-ую')
    print('3. Выход')
    v=int(input())
    if v==1:
        by_10()
    elif v==2:
        in_10() # Сделать эту функцию
    elif v==3:
        break
