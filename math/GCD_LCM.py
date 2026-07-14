numbers = input('Введите ряд чисел через запятую: ').split(', ')
for i, number in enumerate(numbers):
    numbers[i] = int(number)

# НОД
for nod in range(min(numbers), 0, -1):
    for number in numbers:
        if number % nod == 0:
            t=True
        else:
            t=False
            break
    if t:
        print(f'Наибольший общий делитель: {nod}')
        break
# НОК
nok=max(numbers)
while True:
    for number in numbers:
        if nok/number==nok//number:
            t=True
        else:
            t=False
            break
    if t:
        print(f'Наименьшее общее кратное: {nok}')
        break
    nok+=1
