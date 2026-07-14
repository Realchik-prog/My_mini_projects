word=input('Введите имя существительное: ')
letters='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ok=None
for i in word:
    # Проверка на русское слово
    matching=False
    if i in letters:
        matching=True
    if not matching:
        print('Слово должно состоять только из русских букв!')
        break
if matching:
    # Если русское слово, то программа выполняется
    word=word.lower()
    ensoul=None
    def ensoul_chek():
        ensoul=None
        while ensoul==None:
            ensoul = input('Одушевлённое(1) или неодушевлённое(2)?: ')
            if ensoul=='1':
                ensoul=True
            elif ensoul=='2':
                ensoul=False
            else:
                ensoul=None
                print('Неправильный ввод!')
    declension=None
    divergent=("время", "имя", "знамя", "пламя", "племя", "семя", "стремя", "темя", "бремя", "вымя", "дитя", "путь")
    for i in divergent:
        if word==i:
            declension="разносклоняемое"
            print(f'{word} -{declensions} существительное')
            break
    if declension==None:
        if word[len(word)-1]=='а' or word[len(word)-1]=='я':
            declension=1
        elif word[len(word)-1]=='о':
            declension=2
            ok = 'о'
        elif word[len(word)-1]=='е':
            declension = 2
            ok = 'e'
        else:
            if word[len(word)-1]=='ь':
                exceptions=("конь", "огонь", "корень", "якорь", "соболь", "гвоздь", "календарь", "инвентарь", "автомобиль", "пень", "кремень", "камень", "толь", "тюль", "тополь", "корабль", "дирижабль", "руль", "олень", "ячмень", "парень", "шкворень", "пельмень", "тюлень", "шмель", "штемпель", "щавель", "киль", "осокорь", "ларь", "пономарь", "билль", "гриль", "тролль", "король")
                for i in exceptions:
                    if word==i:
                        declension=2
                        ok = 'ь'
                        break
                if declension==None:
                    declension=3
            else:
                consonant=("б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ")
                if word[len(word)-1] in consonant:
                    declension=2
                    ok='нулевое'
        if declension==None:
            print('Не удалось определить склонение')
        else:
            print(f'{word} - существительное {declension}-го склонения')

    if declension!=None:
        # Склонение по падежам
        IP=RP=DP=VP=TP=PP=None
        IP = word
        if declension==1:
            if word[len(word)-1]=='я':
                RP=word[0:len(word)-1]+'и'
                DP=word[0:len(word)-1]+'е'
                VP=word[0:len(word)-1]+'ю'
                TP=word[0:len(word)-1]+'ей'
                PP='о ' + word[0:len(word)-1]+'е'
            if word[len(word)-1]=='а':
                if word[len(word)-2]=='ш' or word[len(word)-2]=='ж' or word[len(word)-2]=='к':
                    RP=word[0:len(word)-1]+'и'
                else:
                    RP = word[0:len(word) - 1] + 'ы'
                DP=word[0:len(word)-1]+'е'
                if word[len(word) - 2] == 'ш' or word[len(word) - 2] == 'ж' or word[len(word)-2]=='к':
                    VP=word[0:len(word)-1]+'у'
                else: VP=word[0:len(word)-1]+'ю'
                TP=word[0:len(word)-1]+'ей'
                PP='о ' + word[0:len(word)-1]+'е'
        elif declension==2:
            if ok=='нулевое':
                RP=word+'a'
                DP=word+'у'
                ensoul_chek()
                if ensoul:
                    VP=word+'а'
                else:
                    VP=word
                TP=word+'ом'
                PP='о '+word+'е'
            elif ok=='о':
                RP=word[0:len(word)-1]+'а'
                DP=word[0:len(word)-1]+'у'
                VP=word
                TP=word[0:len(word)-1]+'ом'
                PP='о ' + word[0:len(word)-1]+'е'
            elif ok=='e':
                RP = word[0:len(word) - 1] + 'я'
                DP = word[0:len(word) - 1] + 'ю'
                VP = word
                TP = word[0:len(word) - 1] + 'ем'
                if word[len(word)-2]=='и':
                    PP='о ' + word[0:len(word)-1]+'и'
                else:
                    PP = 'о ' + word
            elif ok=='ь':
                print('Склонение этого слова по падежам смотри в интернете')
        elif declension==3:
            RP=DP=word[0:len(word)-1]+'и'
            PP='о '+word[0:len(word)-1]+'и'
            VP=word
            TP=word+'ю'



    print(f'И.П. {IP}')
    print(f'Р.П. {RP}')
    print(f'Д.П. {DP}')
    print(f'В.П. {VP}')
    print(f'Т.П. {TP}')
    print(f'П.П. {PP}')
