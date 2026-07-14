print('Эта программа определяет, может ли король попасть с первой клетки на вторую одним ходом')

x1= int(input('Введите координату x клетки 1: '))
y1= int(input('Введите координату y клетки 1: '))
x2= int(input('Введите координату x клетки 2: '))
y2= int(input('Введите координату y клетки 2: '))
for coordinate in [x1,y1,x2,y2]:
    if coordinate>8 or coordinate<1:
        raise ValueError('Координаты клетки могут быть заданы только в диапазоне от 1 до 8!')
can_move=False
for good_x in range(x1-1, x1+2):
    if can_move:
        break
    if good_x==x2:
        for good_y in range(y1-1, y1+2):
            if good_y==y2:
                can_move=True
                break
if x1==x2 and y1==y2:
    can_move=False

if can_move:
    print('Да')
else:
    print('Нет')