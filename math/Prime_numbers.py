print('Приветствую в программе для простых чисел!')
while True:
    print()
    print('Команды:')
    print('1. Вывести список простых чисел')
    print('2. Вывести простое число n-ого номера по счёту')
    print('3. Выйти')
    print()
    input_command=int(input('Введите цифру команды: '))
    if input_command==3:
        break
    elif input_command==1:
        a=int(input('Сколько простых чисел вывести?: '))
        if a<1:
            print('Неправильный ввод')
        else:
            n=1
            numbers=[2]
            i=2
            # i - число для проверки на простоту
            while n<a:
                i+=1
                for j in numbers:
                    if i%j!=0:
                        simple=True
                    else:
                        simple=False
                        break
                if simple:
                    numbers.append(i)
                    n+=1
            print(f'Ответ: {numbers}')
    elif input_command==2:
        a=int(input('Какое по счёту простое число вывести?: '))
        if a<1:
            print('Неправильный ввод')
        else:
            n=1
            numbers=[2]
            i=2
            # i - число для проверки на простоту
            while n<a:
                i+=1
                for j in numbers:
                    if i%j!=0:
                        simple=True
                    else:
                        simple=False
                        break
                if simple:
                    numbers.append(i)
                    n+=1
            print(f'Ответ: {numbers[a-1]}')
    
