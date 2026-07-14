z = True
while z:
    d=int(input('Введите число проверки кратности:'))
    if d==1:
        print('Любые числа кратны единице')
    elif d<=0:
        print('Только натуральные числа!')
    else:
        z = False
        a=int(input('Введите a:'))
        b=int(input('Введите b:'))
        c=int(input('Введите c:'))
        if a%d==0 and b%d==0 and c%d==0:
            print(a,b,c,'кратны',d)
        else:
            print(a,b,c, 'вместе не кратны',d)


