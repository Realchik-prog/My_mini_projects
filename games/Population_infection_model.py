from time import sleep
from math import sqrt
from random import randint
while True:
    try:
        all_people = int(input('Введите, сколько людей будет жить на Земле: '))
        if all_people <= 0:
            print('Число людей должно быть положительно')
            continue
        all_infected_people = int(input('Введите, сколько будет заражённых: '))
        if all_infected_people > all_people:
            print('Заражённых не может быть больше, чем всего людей')
            continue
        if all_infected_people <= 0:
            print('Число заражённых должно быть положительно')
            continue
        break
    except ValueError:
        print('Неправильный ввод')
day = 0
print(f'День 0')
print(f'{all_infected_people} заражённых')
while True:
    print()
    if day !=0:
        recovered_people_k *= 1.2
        recovered_people = round(all_infected_people//5 + recovered_people_k//3)
    else:
        recovered_people = 0
        recovered_people_k = 1.2
    all_infected_people_update = round(all_infected_people * 1.5) + randint(round(-sqrt(all_infected_people//2)), round(sqrt(all_infected_people)))
    day_infected_people = all_infected_people_update - all_infected_people
    all_infected_people = all_infected_people_update - recovered_people
    sleep(1)
    day += 1
    print(f'День {day}')
    if recovered_people != 0:
        print(f'Выздоровело: {recovered_people} человек')
    if day_infected_people != 0:
        print(f'Заразилось: {day_infected_people} человек')
    if all_infected_people > 0:
        print(f'{all_infected_people if all_infected_people < all_people else all_people} заражённых всего')
    else:
        print('Заражённых не осталось')
        break
    if all_infected_people >= all_people:
        print('Инфекция заразила всех людей')
        break