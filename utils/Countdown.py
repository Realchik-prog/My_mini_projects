from time import sleep
while True:
    try:
        timer = int(input('Введите количество секунд: '))
        if timer <= 0:
            print('Неположительное число!')
        else:
            break
    except ValueError:
        print('Неправильный ввод!')
for second in range(timer, 0, -1):
    print(second)
    sleep(1)
print('Конец отсчёта!')