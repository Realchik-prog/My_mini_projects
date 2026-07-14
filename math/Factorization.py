a=int(input('Какое число хотите разложить на множители?: '))
if a <= 1:
    print('Неправильный ввод')
else:
    b=a
    i=1
    m = []
    simple_numbers = []
    simple=True
    while b!=1:
        i += 1
        for j in simple_numbers:
            if i % j != 0:
                simple = True
            else:
                simple = False
                break
        if simple:
            simple_numbers.append(i)
            s=True
            while s:
                if b%simple_numbers[len(simple_numbers)-1] == 0:
                    b/=simple_numbers[len(simple_numbers)-1]
                    m.append(simple_numbers[len(simple_numbers)-1])
                else:
                    s=False
    print(f'{a}={m[0]}', end='')
    for i in range(1, len(m)):
        print(f'*{m[i]}', end='')
