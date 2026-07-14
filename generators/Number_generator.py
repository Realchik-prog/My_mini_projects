a=int(input('Введите минимальное значение: '))
b=int(input('Введите максимальное значение: '))
import random
list=[]
for i in range(a, b+1):
    list.append(i)
print(f'Выпало {random.sample(list, i)}')

