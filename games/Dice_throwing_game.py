from random import *
from math import pi
ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8, ev9, ev10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
way = ['Старт']
detected_difficult=False
PS=input('Введите "да", если нужно пояснение игры: ')
if PS=='да':
    print('Вам нужно вернуться домой. Вы бросаете кость и ходите по клеткам в соответствии с выпавшими очками (от 1 до 3). ')
    print('На вашем пути встретяться различные препятствия, которые нужно преодолеть. Они могут быть как хорошие, так и плохие. ')
    print('Некоторые клетки могут отнимать ваши сердца. Вначале у вас их 3. Вы погибните, если они закончатся.')
    print('Также вам придётся принимать различные решения по ходу игры. ')
    print('Выбирайте сложность. Она определяет длину вашего пути. Удачного прохождения!')
print()
while not detected_difficult:
    difficult=int(input('Выберите сложность (Любое натуральное число, желательно немного): '))
    if difficult>0:
        print(f'Сложность {difficult} выбрана')
        detected_difficult=True
    else:
        print('Неправильный ввод')
for i in range(1, 10*difficult+1):
    way.append(None)
    while way[i]==None:
        r=random()
        if r<=0.1 and ev1<difficult:
            way[i]='Дорога'
            ev1+=1
        elif 0.1<r<=0.2 and ev2<difficult:
            way[i]='Клад'
            ev2+=1
        elif 0.2<r<=0.3 and ev3<difficult and i>=3:
            way[i]='Телепорт'
            ev3+=1
        elif 0.3<r<=0.4 and ev4<difficult:
            way[i]='Враг'
            ev4+=1
        elif 0.4<r<=0.5 and ev5<difficult:
            way[i]='Убежище'
            ev5+=1
        elif 0.5<r<=0.6 and ev6<difficult:
            way[i]='Волшебник'
            ev6+=1
        elif 0.6<r<=0.7 and ev7<difficult:
            way[i]='Ловушка'
            ev7+=1
        elif 0.7<r<=0.8 and ev8<difficult:
            way[i]='Лес'
            ev8+=1
        elif 0.8<r<=0.9 and ev9<difficult:
            way[i]='Зелье'
            ev9+=1
        elif 0.9<r<=1 and ev10<difficult:
            way[i]='Озеро'
            ev10+=1
way.append('Дом')

print('Твой путь:')
print('Старт --> ', end='')
for i in range(difficult):
    print(f'{way[1+10*i]} --> {way[2+10*i]} --> {way[3+10*i]} --> {way[4+10*i]} --> {way[5+10*i]} --> {way[6+10*i]} --> {way[7+10*i]} --> {way[8+10*i]} --> {way[9+10*i]} --> {way[10+10*i]} --> ', end='')
print('Дом')
"""
Дорога - нейтральные события
Клад, убежище, волшебник - положительные события
Враг, ловушка, озеро - отрицательные события
Телепорт, зелье, лес - случайные события
"""
way_length=0
money=0
health=3
print('!(У вас 3 сердца)')
Long_run=False
Short_run=False
tele=False
sword=False
k_roll = k_health_up = k_health_down = k_money_up = k_money_down = k_action = 0
def health_chek(up):
    if up:
        global k_health_up
        k_health_up+=1
        if health<5:
            print(f'!(У вас стало {health} сердца)')
        else:
            print(f'!(У вас стало {health} сердцец)')
    elif not up:
        global k_health_down
        k_health_down+=1
        if health>=5:
            print(f'!(У вас осталось {health} сердцец)')
        elif health>=2:
            print(f'!(У вас осталось {health} сердца)')
        elif health==1:
            print('!(У вас осталось 1 сердце)')
        else:
            print('Вы истратили все сердца и погибли!')
def money_chek(up):
    if up:
        global k_money_up
        k_money_up+=1
        if money>=5:
            print(f'!(У вас стало {money} монет)')
        elif money>1:
            print(f'!(У вас стало {money} монеты)')
        elif money==1:
            print('!(У вас теперь 1 монета)')
    elif not up:
        global k_money_down
        k_money_down+=1
        if money>=5:
            print(f'!(У вас осталось {money} монет)')
        if money>=2:
            print(f'!(У вас осталось {money} монеты)')
        elif money==1:
            print('!(У вас осталась 1 монета)')
        else:
            print('!(У вас не осталось монет)')
p=(round((difficult)**pi*1000000))%10000
while way_length!=difficult*10+1 and health!=0:
    # Прохождение пути
    print()
    if not tele:
        # Бросок кости
        roll=input('Бросить кость:')
        k_roll+=1
        if Long_run:
            Long_run=False
            if random()<1/3:
                way_length+=2
                print('Выпало 2 очка!')
            elif random()<2/3:
                way_length+=3
                print('Выпало 3 очка!')
            else:
                way_length+=4
                print('Выпало 4 очка!')
        elif Short_run:
            Short_run=False
            way_length+=1
            print('Выпало 1 очко!')
        elif roll!=None:
            if random()<1/3:
                way_length+=1
                print('Выпало 1 очко!')
            elif random()<2/3:
                way_length+=2
                print('Выпало 2 очка!')
            else:
                way_length+=3
                print('Выпало 3 очка!')
    elif tele:
        # При телепорте бросок кости пропускается
        tele=False

    # Показ клеток
    if way_length>difficult*10+1:
        way_length=difficult*10+1
    if difficult*10+1-way_length>3:
        print(f'Вы попали на клетку {way[way_length]} ( Далее: --> {way[way_length+1]} --> {way[way_length+2]} --> {way[way_length+3]} --> {way[way_length+4]})')
    elif difficult*10+1-way_length==3:
        print(f'Вы попали на клетку {way[way_length]} ( Далее: --> {way[way_length+1]} --> {way[way_length+2]} --> {way[way_length+3]})')
    elif difficult*10+1-way_length==2:
        print(f'Вы попали на клетку {way[way_length]} ( Далее: --> {way[way_length+1]} --> {way[way_length+2]})')
    elif difficult*10+1-way_length==1:
        print(f'Вы попали на клетку {way[way_length]} ( Далее: --> {way[way_length+1]})')
    elif difficult*10+1-way_length==0:
        print(f'Вы вернулись домой!')
        break
    # События
    if way[way_length]=='Дорога':
        # Дорога
        print('Вы спокойно идёте дальше')
    elif way[way_length]=='Клад':
        # Клад
        money+=1
        print('Вы нашли 1 монету!')
        money_chek(True)
    elif way[way_length]=='Убежище':
        # Убежище
        print('Вы переждали время и теперь ваш следующий ход увеличен дополнительно на 1 клетку')
        Long_run=True
    elif way[way_length]=='Волшебник':
        # Волшебник
        if random()<0.5:
            health+=1
            print('Волшебник даровал вам дополнительное сердце!')
            health_chek(True)
        else:
            print('Волшебник решил, что вы не заслужили дополнительное сердце')
    elif way[way_length]=='Враг':
        # Враг
        if not sword:
            vrag=None
            print('Вы встретили мужика, которому нужна в долг одна ваша монета!')
            k_action+=1
            while vrag!='дать монету' and vrag!='бежать':
                vrag=input('?(дать монету/бежать): ')
                if vrag=='дать монету':
                    if money==0:
                        health-=1
                        print('Вы выворачиваете карманы, но у вас ничего не оказалось. Bас избили')
                        health_chek(False)
                    elif money>=1:
                        money-=1
                        print('Вы дали ему монету и он от вас отстал')
                        money_chek(False)
                elif vrag=='бежать':
                    if random()<0.5:
                        print('Вы смогли скрыться')
                    else:
                        health-=1
                        print('Вас догнали и избили')
                        health_chek(False)
                else:
                    print('Неправильный ввод')
        else:
            print('Вы испугали мужика мечом')
    elif way[way_length]=='Ловушка':
        # Ловушка
        if not sword:
            print('Вы попались!')
            lovushka=None
            k_action+=1
            while lovushka!='кричать' and lovushka!='выбираться':
                lovushka=input('?(кричать/выбираться): ')
                if lovushka=='кричать':
                    if random()<0.5:
                        health-=1
                        print('На крик пришёл хозяин ловушки и поколечил вас')
                        health_chek(False)
                        if health>0:
                            print('Вы смогли сбежать')
                    else:
                        print('На крик пришли спасатели и вытащили вас, вы пошли дальше')
                elif lovushka=='выбираться':
                    print('Вы смогли выбраться, но сильно устали. Следующий ход только на 1 клетку!')
                    Short_run=True
                else:
                    print('Неправильный ввод')
        else:
            print('Вы разрубили ловушку мечом и двинулись дальше')
    elif way[way_length]=='Озеро':
        # Озеро
        print('Можно плыть самостоятельно, либо арендовать лодку на этот путь за 2 монеты')
        k_action+=1
        ozero=None
        while ozero!='плыть' and ozero!='арендовать лодку':
                ozero=input('?(плыть/арендовать лодку): ')
                if ozero=='плыть':
                    Short_run=True
                    if random()<0.5:
                        print('Вы смогли переплыть, но устали. Следующий ход только на 1 клетку!')
                    else:
                        print('Озеро оказалось слишком холодным. Вы простудились, потеряв одно сердце', end='')
                        health-=1
                        if health>0:
                            print('. Из-за усталости следующий ход только на одну клетку!')
                        else:
                            print()
                        health_chek(False)
                elif ozero=='арендовать лодку':
                    if money>=2:
                        print('Вы арендовали лодку и успешно переплыли на ней озеро')
                        money-=2
                        money_chek(False)
                    else:
                        print('У вас не хватает монет')
                        ozero=None
                else:
                    print('Неправильный ввод')
    elif way[way_length]=='Телепорт':
        # Телепорт
        print('Вы случайным образом можете переместиться либо назад, либо вперёд на 3 клетки')
        print(f'(До этого было: {way[way_length-3]} --> {way[way_length-2]} --> {way[way_length-1]} -->)')
        teleport=None
        k_action+=1
        while teleport!='использовать' and teleport!='пропустить':
            teleport=input('?(использовать/пропустить): ')
            if teleport=='использовать':
                tele=True
                if random()<0.5:
                    print('Вас переместило на 3 клетки назад')
                    way_length-=3
                    if way_length<0:
                        way_length=0
                else:
                    print('Вас переместило на 3 клетки вперёд')
                    way_length+=3
            elif teleport!='пропустить':
                print('Неправильный ввод')
    elif way[way_length]=='Зелье':
        # Зелье
        print('Вы подобрали зелье и вы не знаете, что оно даёт')
        zelie=None
        k_action+=1
        while zelie!='выпить' and zelie!='бросить':
            zelie=input('?(выпить/бросить): ')
            if zelie=='выпить':
                r=random()
                if r<=0.25:
                    health-=1
                    print('Зелье отняло у вас одно сердце')
                    health_chek(False)
                elif r<=0.5:
                    health+=1
                    print('Зелье дало вам одно сердце')
                    health_chek(True)
                elif r<=0.75:
                    Long_run=True
                    print('Зелье сделало ваш следующий ход на одну клетку дальше')
                elif r<=1:
                    tele=True
                    print('Зелье телепортировало вас', end='')
                    if random()<0.5:
                        print(' на 1 клетку назад')
                        way_length-=1
                        if way_length<0:
                            way_length=0
                    else:
                        print(' на 1 клетку вперёд')
                        way_length+=1
            elif zelie!='бросить':
                print('Неправильный ввод')
    elif way[way_length]=='Лес':
        # Лес
        if random()<0.5:
            print('Вы прошли сквозь тёмный лес и ничего не случилось')
        else:
            if random()<0.5:
                if not sword:
                    print('Вы встретили волков и они вас покусали')
                    health-=1
                    health_chek(False)
                else:
                    print('Вы встретили волков и разогнали их мечом')
            else:
                if difficult>=6:
                    if not sword:
                        print('Вы встретили меч, но чтобы его забрать, нужен код')
                        password=input('! Введите код: ')
                        if password==str(p):
                            print('Вы смогли забрать меч!')
                            sword=True
                        else:
                            print('Код неправильный. Вы ушли без меча')
                    else:
                        print('Вы круто размахиваетесь мечом')
                else:
                    print('Вы прошли сквозь тёмный лес и ничего не случилось')

                
        
                
                    
                
                    
                    





# Концовка

if health>=1: print('Поздравляю с победой!')
if not sword: sword_chek='Не взят'
else: sword_chek='Взят'

print()
# Статистика
print('Статистика за игру:')
print(f'Бросков кости: {k_roll}')
print(f'Сделано действий: {k_action}')
print(f'Пройдено клеток: {way_length}/{len(way)-1}')
print(f'Получено сердец: {k_health_up}')
print(f'Осталось сердец: {health}')
print(f'Потрачено сердец: {k_health_down}')
print(f'Получено монет: {k_money_up}')
print(f'Осталось монет: {money}')
print(f'Потрачено монет: {k_money_down}')
if difficult>=6:
    print(f'Меч: {sword_chek}')
else:
    print(f'???: {sword_chek}')
print()

# Комментарий концовки
if health>0 and difficult>=6 and not sword:
    print(f'Вы прошли достаточно трудную сложность. Код от меча на сложности {difficult}: {p}. Используйте его в следующий раз')
elif health>0 and difficult>=6:
    print('Ставьте сложность выше и бейте свои и чужие рекорды!')
elif health>0:
    print('Поздравляю с победой! Подсказка: пройдите сложность 6 или выше для разблокировки нового события')
else:
    print('Может, в следующей игре у вас получится победить?')
        
