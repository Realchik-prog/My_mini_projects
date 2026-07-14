print('Представляю игру Верно/неверно! Нужно угадать верно ли равенство')
from random import *
count = 0
while count<5:
    b=round(random()*10)
    a=round(random()*10)
    count+=1
    count1=0
    r=random()
    e=round(random()*10)
    if random()<0.5:
        c=1
    else:
        c=-1
    if random()<0.5:
        d=1
    else:
        d=-1
    while count1<1:
        if r<0.5:
            print(b,'+',a*c,'=',b+a*c)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                print('Правильно')
                print('До победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    count-=2
                    print('Неправильно')
                    print('Теперь до победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
        else:
            print(b,'+',a*c,'=',b+a*c+(e+1)*d)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                count-=2
                print('Неправильно')
                print('Теперь до победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    print('Правильно')
                    print('До победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
print("Теперь числа станут сложнее!")
while count<10:
    b=round(random()*100)
    a=round(random()*100)
    count+=1
    count1=0
    r=random()
    e=round(random()*10)
    if random()<0.5:
        c=1
    else:
        c=-1
    if random()<0.5:
        d=1
    else:
        d=-1
    while count1<1:
        if r<0.5:
            print(b,'+',a*c,'=',b+a*c)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                print('Правильно')
                print('До победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    count-=2
                    print('Неправильно')
                    print('Теперь до победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
        else:
            print(b,'+',a*c,'=',b+a*c+(e+1)*d)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                count-=2
                print('Неправильно')
                print('Теперь до победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    print('Правильно')
                    print('До победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
print("Теперь числа станут ЕЩЁ сложнее!")
while count<15:
    b=round(random()*1000)
    a=round(random()*1000)
    count+=1
    count1=0
    r=random()
    e=round(random()*10)
    if random()<0.5:
        c=1
    else:
        c=-1
    if random()<0.5:
        d=1
    else:
        d=-1
    while count1<1:
        if r<0.5:
            print(b,'+',a*c,'=',b+a*c)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                print('Правильно')
                print('До победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    count-=2
                    print('Неправильно')
                    print('Теперь до победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
        else:
            print(b,'+',a*c,'=',b+a*c+(e+1)*d)
            s=input('Это верно?(да/нет) ')
            if s=='да':
                count-=2
                print('Неправильно')
                print('Теперь до победы надо угадать',15-count)
                count1+=1
            else:
                if s=='нет':
                    print('Правильно')
                    print('До победы надо угадать',15-count)
                    count1+=1
                else:
                    print('Некорректный ответ, попробуйте ещё раз')
print('Вы выиграли!')
