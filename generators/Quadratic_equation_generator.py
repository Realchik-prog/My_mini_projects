from random import *

print('Это генератор квадратных уравнений!')
n=int(input('Сколько уравнений хотите сгенерировать?: '))
result=[]
i=0
while i!=n:
    a=0
    while a==0:
        if random()>0.5:
            a=int(random()*100)
        else:
            a=-1*int(random()*100)
    if random()>0.5:
        b=int(random()*100)
        b1='+'+str(b)
    else:
        b=-1*int(random()*100)
        b1=b
    if random()>0.5:
        c=int(random()*100)
        c1='+'+str(c)
    else:
        c=-1*int(random()*100)
        c1=c
    if c==0:
        c1='+0'
    if b==0:
        b1='+0'
        
    D=b**2-4*a*c
    if D>0:
        x1=(-b-D**0.5)/(2*a)
        x2=(-b+D**0.5)/(2*a)
        if x1==int(x1) and x2==int(x2):
            result.append(f'x1={int(x1)}, x2={int(x2)}')
            print(f'{i+1}) {a}x^2{b1}x{c1}=0')
            i+=1
    elif D==0:
        x=-b/(2*a)
        if x==int(x):
            result.append(f'x={int(x)}')
            print(f'{i+1}) {a}x^2{b1}x{c1}=0')
            i+=1

f=input('Показать решение?: ')
if f=='да' or f=='Да':
    for i in range(len(result)):
        print(f'{i+1}) {result[i]}')
   
    
