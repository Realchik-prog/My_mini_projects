from turtle import *
a=int(input('Введите сид генерации рисунка: '))
i=1
screensize(10000, 10000)
while True:
    forward(1)
    if i%50==0:
        left((90*(i/a))%360)
    i+=1

    
