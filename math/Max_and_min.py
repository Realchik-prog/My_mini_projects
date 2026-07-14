print('Вводите числа. Чтобы остановить, введите 0')
a=int(input())
k=a
m=a
while a!=0:
    k=max(a,k)
    m=min(a,m)
    a=int(input())
print(k, m)
