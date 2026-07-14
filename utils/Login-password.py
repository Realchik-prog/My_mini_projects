import pandas as pd
accounts = {}
def registration():
    global accounts
    while True:
        login = input('Введите логин: ')
        if login in accounts:
            print('Такой логин уже был взят')
            continue
        while True:
            password = input('Установите пароль: ')
            if len(password)<=3:
                print('Данный пароль слишком лёгкий')
                continue
            break
        accounts[login] = {
            'пароль': password,
            'содержание': ''
        }
        print('Аккаунт успешно зарегистрирован')
        break
    account_menu(login)
def account_menu(login):
    global accounts
    print(f'Здравствуйте, {login}!')
    while True:
        print('Меню аккаунта:')
        print('1. Содержание')
        print('2. Настройки аккаунта')
        print('3. Выход из аккаунта')
        a = input()
        if a == '1':
            while True:
                if len(accounts[login]['содержание'])==0:
                    print('В содержании ничего нет')
                    print('1. Добавить содержание')
                else:
                    print(f'"{accounts[login]['содержание']}"')
                    print('1. Изменить содержание')
                print('2. Удалить содержание')
                print('3. Выход из содержания')
                a = input()
                if a == '1':
                    accounts[login]['содержание']=input('Введите содержание: ')
                    print('Содержание сохранено')
                elif a == '2':
                    accounts[login]['содержание']=''
                    print('Содержание удалено')
                elif a == '3':
                    break
        elif a=='2':
            while True:
                print('1. Сменить логин')
                print('2. Сменить пароль')
                print('3. Удалить аккаунт')
                print('4. Выход из настроек')
                a = input()
                if a == '1':
                    while True:
                        new_login = input('Введите новый логин: ')
                        if new_login in accounts:
                            print('Такой логин уже был взят')
                            continue
                        accounts[new_login] = {
                            'пароль': accounts[login]['пароль'],
                            'содержание': accounts[login]['содержание']
                        }
                        del accounts[login]
                        login=new_login
                        print('Логин успешно изменён')
                        break
                elif a == '2':
                    while True:
                        new_password = input('Введите новый пароль: ')
                        if len(new_password)<=3:
                            print('Данный пароль слишком лёгкий')
                            continue
                        accounts[login]['пароль']=new_password
                        print('Пароль успешно изменён')
                        break
                elif a == '3':
                    if input('Вы точно хотите удалить аккаунт? (да/нет): ').lower()=='да':
                        del accounts[login]
                        print('Аккаунт успешно удалён!')
                        break
                elif a=='4':
                    break
        elif a=='3':
            break
        if login not in accounts:
            break
def access():
    global accounts
    if len(accounts)==0:
        print('Ни одного аккаунта не создано')
        return None
    while True:
        login = input('Введите логин: ')
        if login not in accounts:
            print('Такого логина не существует')
            continue
        while True:
            password = input('Введите пароль: ')
            if accounts[login]['пароль']!=password:
                print('Пароль не подходит')
                continue
            break
        print('Вы успешно зашли в аккаунт')
        break
    account_menu(login)
print('Приветствую в программе "Логин-пароль"!')
while True:
    print('Меню:')
    print('1. Регистрация аккаунта')
    print('2. Вход в аккаунт')
    print('3. Существующие аккаунты')
    print('4. Вход в панель админа')
    print('5. Выход из программы')
    a = input()
    if a == '1':
        registration()
    elif a=='2':
        access()
    elif a=='3':
        if len(accounts)>0:
            print('Все аккаунты:')
            for i in accounts:
                print(f'* {i}')
        else:
            print('Аккаунтов нет')
    elif a=='4':
        while True:
            print('Меню админа: ')
            print('1. Посмотреть содержания всех аккаунтов')
            print('2. Удалить все аккаунты')
            print('3. Выход из панели админа')
            a = input()
            if a == '1':
                print(pd.DataFrame(accounts))
            elif a == '2':
                accounts={}
                print('Все аккаунты успешно удалены')
            elif a == '3':
                break
    elif a=='5':
        break