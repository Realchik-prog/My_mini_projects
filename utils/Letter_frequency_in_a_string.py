a = input('Введите строку: ')
b = {}
for char in a:
    if char.lower() not in b:
        b[char.lower()] = a.count(char.lower()) + a.count(char.upper())
print('Количество каждой буквы в строке:')
if ' ' in b:
    del b[' ']
while len(b) > 0:
    value = None
    for k, v in b.items():
        if all(v >= count for count in b.values()):
            value = v
            key = k
            print(f'"{k}"', end='')
            break
    a=[]
    del b[key]
    for k, v in b.items():
        if v == value:
            print(f', "{k}"', end='')
            a.append(k)
    for k in a:
        del b[k]
    print(f' : {value}')