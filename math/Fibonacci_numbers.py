def fibonacci(n):
    def fibonacci_(m):
        return list_fibonacci[m - 2] + list_fibonacci[m - 1]
    list_fibonacci = [0, 1]
    while True:
        if n==0:
            return 0
        if n==1:
            return 1
        if len(list_fibonacci) < n:
            list_fibonacci.append(fibonacci_(len(list_fibonacci)))
        else:
            return fibonacci_(n)
while True:
    try:
        print('1. n-ое число Фибоначчи')
        print('2. Все числа Фибоначчи до заданного по счёту')
        print('3. Все числа Фибоначчи до заданного числа')
        print('0. Выход из программы')
        mode = input('Выберите действие: ').strip()
        if mode=='1':
            n = int(input('Введите номер числа Фибоначчи: '))
            if n<1:
                raise ValueError
            elif n>10000:
                print('Не советую пробовать такие большие числа! Это может плохо закончиться')
            else:
                print(fibonacci(n-1))
        elif mode=='2':
            n = int(input('Введите количество чисел Фибоначчи: '))
            if n<0:
                raise ValueError
            elif n>10000:
                print('Не советую пробовать такие большие числа! Это может плохо закончиться')
            for i in range(n):
                print(f'{i+1}. {fibonacci(i)}')
        elif mode=='3':
            m = int(input('Введите число, до которого будут выведены все числа Фибоначчи: '))
            if m<0:
                raise ValueError
            for i in range(m):
                f = fibonacci(i)
                if f <= m:
                    print(f'{i+1}. {f}')
                else:
                    break
        elif mode=='0':
            break
    except ValueError:
        print('Кажется, вы ввели неправильное число/не число')
