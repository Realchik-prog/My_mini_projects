russian_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
english_letters = list('abcdefghijklmnopqrstuvwxyz')
upper_chars = []
word = input('Введите строку: ')
for index, char in enumerate(word):
    if char.upper() == char and char.lower() != char:
        upper_chars.append(index)
word = list(word.lower())
while True:
    try:
        shift = int(input('На какой сдвиг хотите сместиться?: '))
        break
    except ValueError:
        print('Неправильный ввод')
shift_switch = []
shift_switch.append(input('Делать сдвиг внутри двойных кавычек?: ').lower() == 'да')
shift_switch.append(input('Делать сдвиг внутри скобок?: ').lower() == 'да')
with_shift = [True, True]
for index, char in enumerate(word):
    if char == '"' and not shift_switch[0]:
        with_shift[0] = not with_shift[0]
    elif char in '()' and not shift_switch[1]:
        with_shift[1] = not with_shift[1]
    elif with_shift[0] and with_shift[1]:
        for count, letter in enumerate(russian_letters):
            if char == letter:
                word[index] = russian_letters[(count+shift)%len(russian_letters)]
        for count, letter in enumerate(english_letters):
            if char == letter:
                word[index] = english_letters[(count+shift)%len(english_letters)]
    if index in upper_chars:
        word[index] = word[index].upper()
print(''.join(word))