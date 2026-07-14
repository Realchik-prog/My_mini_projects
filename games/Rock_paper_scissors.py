from random import choice
from time import sleep

print('Это сражение с компьютером в "Камень, ножницы, бумага"!')
while True:
    try:
        rounds = int(input('Сколько будет раундов?: '))
        if rounds <= 0:
            print('Неположительное число')
        else:
            break
    except ValueError:
        print('Неправильный ввод')
player_count = computer_count = 0
for i in range(1, rounds+1):
    print()
    print(f'РАУНД {i}/{rounds}')
    sleep(1)
    while True:
        player = input('Введите предмет: ')
        if player.lower()=='камень' or player.lower()=='ножницы' or player.lower()=='бумага':
            break
        else:
            print('Неправильный ввод')
    computer = choice(['камень', 'ножницы', 'бумага'])
    print(f'{player} vs {computer}')
    sleep(1)
    if player == computer:
        print('Ничья')
    elif player == 'камень' and computer == 'ножницы' or player == 'ножницы' and computer == 'бумага' or player == 'бумага' and computer == 'камень':
        print('Вы выиграли раунд')
        player_count += 1
    else:
        print('Компьютер выиграл раунд')
        computer_count += 1
    sleep(1)
    if i!=rounds:
        print(f'Счёт {player_count}:{computer_count}', end='')
        if player_count > computer_count:
            print(' в вашу пользу')
        elif player_count < computer_count:
            print(' в пользу компьютера')
        else:
            print(' в ничью')
    else:
        print()
        print(f'Финальный счёт {player_count}:{computer_count}')
    sleep(1)
if player_count == computer_count:
    print('Вы сыграли в ничью!')
elif player_count > computer_count:
    print('Вы одержали победу!')
else:
    print('Вы проиграли!')





