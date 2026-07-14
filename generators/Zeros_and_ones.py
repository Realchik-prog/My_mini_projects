from random import *
for i in range(int(input('Сколько символов сгенерировать?: '))):
    if random()<0.5: print(0, end='')
    else: print(1, end='')
