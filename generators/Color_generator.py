from random import choice, randint
print('Форматы: ')
print('1. RGB')
print('2. HEX16')
print()
while True:
    mode = input('Выберите формат для генерации цвета (цифра): ')
    if mode=='1':
        mode = 'RGB'
    elif mode=='2':
        mode = 'HEX16'
    else:
        print('Неправильный ввод')
        continue
    break
while True:
    try:
        count = int(input('Сколько будет сгенерировано цветов?: '))
        if count < 1:
            raise ValueError
        break
    except ValueError:
        print('Неправильный ввод')
if mode=='RGB':
    for i in range(1, count + 1):
        color = [randint(0,255), randint(0,255), randint(0,255)]
        print(f'{i}) {color[0]} {color[1]} {color[2]}')
elif mode=='HEX16':
    for i in range(1, count + 1):
        color = ''
        for _ in range(6):
            color += choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])
        print(f'{i}) #{color}')