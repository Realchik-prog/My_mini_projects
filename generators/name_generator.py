from random import randint, choice

alphabet = {
    'гласные': 'уеыаоэяиюё',
    'согласные': {
        'звонкие': 'йцнгзврлджмб',
        'глухие': 'кшщхфчпст',
        'все': 'йцнгзврлджмбкшхфчпст' # без щ :(
        }
}


print('Это программа "Генератор имени"!\n')
print('Настройки')
while True:
    try:
        length = input('Введите количество символов в имени (Промежуток через "-" или число): ').split('-')
        if len(length) == 1:
            length = int(length[0])
        elif len(length) == 2:
            length = (int(length[0]), int(length[1]))
        else:
            raise ValueError
        break
    except:
        print('Неправильный ввод')
while True:
    try:
        names_number = int(input('Сколько имён сгенерировать?: '))
        break
    except ValueError:
        print('Неправильный ввод')
print()
def create_name(length) -> str:
    if type(length) == tuple:
        length = randint(length[0], length[1])
    name: list[str] = []
    for index in range(length):
        possible = None
        try:
            if index == 0:
                possible = 'уеаоэяию' + alphabet['согласные']['все']
                continue
            if index == length - 1:
                if name[-1] in alphabet['согласные']['все'] and name[-1] not in 'йщц':
                    possible = 'ая' + 'ььь'
                elif name[-1] in 'й':
                    possible = 'тнвлдм'
                elif name[-1] in 'щц':
                    possible = 'а'
                else:
                    possible = alphabet['согласные']['все']
                continue
            if name[-1] in alphabet['гласные']:
                if name[-1] in 'аоэи':
                    possible = alphabet['согласные']['все'] + 'я'
                possible =  alphabet['согласные']['все'] + ''
            elif name[-1] == 'й':
                possible = 'уаоэ'
            elif name[-1] in 'цщч':
                possible = 'уиао'
            elif name[-1] in 'нрл':
                possible = alphabet['гласные']
            elif name[-1] in 'гмк':
                possible = 'нрл' + alphabet['гласные']
            elif name[-1] in 'бвп':
                possible = 'рл' + alphabet['гласные']
            elif name[-1] in 'д':
                possible = 'врл' + alphabet['гласные']
            elif name[-1] in 'з':
                possible = 'внл' + alphabet['гласные']
            elif name[-1] in 'ж':
                possible = 'др' + alphabet['гласные']
            elif name[-1] in 'ш':
                possible = 'кврлмтуиао'
            elif name[-1] in 'х':
                possible = 'рл' + alphabet['гласные']
            elif name[-1] in 'ф':
                possible = 'рлтн' + alphabet['гласные']
            elif name[-1] in 'с':
                possible = 'рлнмкпт' + alphabet['гласные']
            elif name[-1] in 'т':
                possible = 'вр' + alphabet['гласные']
                    
        finally:
            if possible is None:
                print(name[-1])
                raise ValueError
            char = choice(list(possible))
            name.append(char)
            
    if set(name) & set(alphabet['гласные']) != set():
        return ''.join(name).title()
    else:
        return create_name(length)
for _ in range(names_number):
    name = create_name(length)
    print(name)

