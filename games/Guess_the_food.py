import random

possible = {'лайм', 'банан', 'апельсин', 'черника', 'арбуз', 'клубника', 'огурец', 'помидор', 'картошка', 'груша', 'баклажан', 'ананас'}
print('Это игра "Загадай еду"! Вы должны будете отвечать да/нет на вопросы от программы')
print(f'Загадайте один из этих предметов: {possible}')
input('(Для старта нажмите ENTER)')
def cutting_off_food(index, possible):
    global questions
    questions[index]['obtained'] = True
    while True:
        print('Осталось предполагаемой еды:', len(possible))
        print(questions[index]['question'])
        a=input().strip()
        if a.lower()=='да':
            return possible & questions[index]['set']
        elif a.lower()=='нет':
            return possible - questions[index]['set']
        else:
            print('Неправильный ввод!')
            return possible
questions=[
    {
        'question': 'Это фрукт?',
        'set': {'лайм', 'банан', 'апельсин', 'груша', 'ананас'}
    },
    {
        'question': 'Это овощ?',
        'set': {'огурец', 'помидор', 'картошка', 'баклажан'}
    },
    {
        'question': 'Это ягода?',
        'set': {'черника', 'арбуз', 'клубника'}
    },
    {
        'question': 'В вашей еде есть красный цвет?',
        'set': {'арбуз', 'клубника', 'помидор'}
    },
    {
        'question': 'В вашей еде есть жёлтый цвет?',
        'set': {'банан', 'картошка', 'груша', 'ананас'}
    },
    {
        'question': 'В вашей еде есть зелёный цвет?',
        'set': {'лайм', 'арбуз', 'огурец', 'груша'}
    },
    {
        'question': 'Ваша еда относится к цитрусовым?',
        'set': {'лайм', 'апельсин'}
    },
    {
        'question': 'В вашей еде есть синий/фиолетовый цвет?',
        'set': {'черника', 'баклажан'}
    },
    {
        'question': 'Вашу еду легко чистить/не надо чистить?',
        'set': {'банан', 'черника', 'клубника', 'огурец', 'помидор', 'груша', 'баклажан'}
    },
    {
        'question': 'Ваша еда круглой/овальной формы?',
        'set': {'лайм', 'апельсин', 'черника', 'арбуз', 'клубника', 'помидор', 'картошка', 'груша', 'ананас'}
    },
    {
        'question': 'Ваша еда сладкая?',
        'set': {'банан', 'черника', 'арбуз', 'клубника', 'груша', 'ананас', 'помидор'}
    }
]
for i in range(len(questions)):
    questions[i]['obtained']=False

while len(possible)>1:
    index = random.randint(0, len(questions)-1)
    if (not questions[index]['obtained']) and possible != possible & questions[index]['set'] != set():
        possible = cutting_off_food(index, possible)
    else:
        questions[index]['obtained'] = True
        is_over = True
        for index in range(len(questions)):
            if not questions[index]['question']:
                is_over = False
        if is_over:
            possible = set()
if len(possible)==1:
    print(f'Это {"".join(possible)}!')
elif len(possible)==0:
    print('Я не смог угадать вашу еду. Возможно вы допустили ошибку в ответах')
