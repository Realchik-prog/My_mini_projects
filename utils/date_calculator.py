from datetime import datetime, date, timedelta
import locale
from sys import platform

def russian_month(date):
    month = date.strftime("%B")
    if month[-1]=='ь' or month[-1]=='й':
        return month[:-1] + 'я'
    else:
        return month + 'а'

if platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'russian_russia')
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

print('Вы запустили калькулятор дат')

now = datetime.now()
print(now.strftime(f"Сейчас: %d {russian_month(now)} %Y года, %H:%M:%S"))

def birthday_calc():
    try:
        birthday = datetime.strptime(input('Введите ваш день рождения (Формат ГГГГ-ММ-ДД): '), '%Y-%m-%d')
        delta = now - birthday
        years = int(delta.days // 365.25)
        print(f'Вам {years} полных лет' + ('. Вы ещё не родились?' if years<0 else ''))
        if years>=0:
            print(f'Дней с дня рождения: {delta.days}')
        else:
            print(f'Дней до дня рождения: {-delta.days}')

        if now >= datetime(now.year, birthday.month, birthday.day):
            next_birthday = datetime(now.year+1, birthday.month, birthday.day)
            until_next_birthday = next_birthday - now
        else:
            next_birthday = datetime(now.year, birthday.month, birthday.day)
            until_next_birthday = now - next_birthday

        if until_next_birthday.days>0:
            print(f'Дней до следующего дня рождения: {until_next_birthday.days}')
        elif until_next_birthday.days==0:
            print(f'Поздравляю! У вас сегодня день рождения!')
    except ValueError:
        print('Ошибка! Некорректный ввод')
def weekday_calc():
    try:
        weekday_date = date.strptime(input("Введите дату в формате ДД.ММ.ГГГГ: "), '%d.%m.%Y')
        print(f'Дата соответствует дню недели "{weekday_date.strftime('%A').title()}"')
    except ValueError:
        print('Ошибка! Некорректный ввод')
def past_and_future():
    delta = timedelta(days=30)
    past_date = (now - delta).strftime('%d.%m.%Y')
    future_date = (now + delta).strftime('%d.%m.%Y')
    print(f'Дата 30 дней назад: {past_date}')
    print(f'Дата через 30 дней от сегодня: {future_date}')
try:
    while True:
        print("""
Панель управления:
  1. Калькулятор дня рождения
  2. Калькулятор дня недели
  3. Прошлое и будущее
  0. Выход
        """)
        mode = input('Введите номер действия: ').strip()
        if mode=='1':
            birthday_calc()
        elif mode=='2':
            weekday_calc()
        elif mode=='3':
            past_and_future()
        elif mode=='0':
            raise KeyboardInterrupt
        else:
            print('Неопознанная команда')
except KeyboardInterrupt:
    print('\nВыход из программы...')
