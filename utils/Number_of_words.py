n=int(input('Сколько абзацев в тексте?: '))
b=[]
for i in range(n):
    a=input('Вводите текст: ').split(' ')
    b+=a
print(b)
print(len(b), 'слов')
