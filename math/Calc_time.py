def f1():
    while True:
        time1=input('Введите первое время "{часы}:{минуты}": ').split(':')
        for i in range(len(time1)):
            time1[i]=int(time1[i])
        if len(time1)==2 and time1[0]<24 and time1[1]<60:
            print('Успешный ввод')
            break
        else:
            print('Неправильный ввод')
    while True:
        time2=input('Введите второе время "{часы}:{минуты}": ').split(':')
        for i in range(len(time2)):
            time2[i]=int(time2[i])
        if len(time2)==2 and time2[0]<24 and time2[1]<60:
            print('Успешный ввод')
            break
        else:
            print('Неправильный ввод')
    time1=time1[0]*60+time1[1]
    time2=time2[0]*60+time2[1]
    time_difference=time2-time1
    if time_difference<0:
        time_difference=24*60+time_difference
    time_difference=[time_difference//60, time_difference%60]
    if time_difference[0]>0 and time_difference[1]>0:
        print(f'Разница: {time_difference[0]} ч {time_difference[1]} мин')
    elif time_difference[0]==0 and time_difference[1]>0:
        print(f'Разница: {time_difference[1]} мин')
    elif time_difference[0]>0 and time_difference[1]==0:
        print(f'Разница: {time_difference[0]} ч')
    elif time_difference[0]==0 and time_difference[1]==0:
        print('Вы ввели одно и то же время')
def f2():
    print('Вводите время в формате "{часы}:{минуты}" и остановите, написав "0:00"')
    all_time=0
    time = input().split(':')
    while time!=['0', '00']:
        for i in range(len(time)):
            time[i]=int(time[i])
        if len(time)==2 and time[1]<60:
            time=time[0]*60+time[1]
            all_time+=time
        else:
            print('Неправильный ввод')
        time = input().split(':')
    hours=all_time//60
    minutes=all_time%60
    if len(str(minutes))==1:
        minutes='0'+str(minutes)
    print(f'Всё время: {hours}:{minutes}')
while True:
    print('Программа для вычисления времени')
    print('Выберите функцию:')
    print('1. Время между двумя значениями времени')
    print('2. Сумма времени')
    print('3. Выход')
    a=int(input())
    if a==1:
        f1()
    elif a==2:
        f2()
    elif a==3:
        break
    else:
        print('Неправильный ввод')

