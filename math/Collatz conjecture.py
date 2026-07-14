number = int(input('Введите положительное число: '))
if number>0:
    print(number, end='')
    while number!=1:
        if number%2==0:
            number//=2
        else:
            number=(3*number+1)
        print(f' --> {number}', end='')
else:
    print('Число не положительное!')