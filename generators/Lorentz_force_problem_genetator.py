from random import choice, randint
elements_list = ['Направление магнитной индукции', 'Направление силы Лоренца', 'Знак частицы', 'Направление движения частицы']
vector_list = ["вправо", "влево", "вверх", "вниз", "к наблюдателю", "от наблюдателя"]
for _ in range(3):
    element_index = randint(0, len(elements_list) - 1)
    element = elements_list[element_index]
    print(element, end=': ')
    del elements_list[element_index]
    if element == 'Направление магнитной индукции' or element == 'Направление силы Лоренца' or element == 'Направление движения частицы':
        vector_index = randint(0, len(vector_list) - 1)
        vector = vector_list[vector_index]
        print(vector)
        for vector_a, vector_b in [("вправо", "влево"), ("вверх", "вниз"), ("к наблюдателю", "от наблюдателя")]:
            if vector == vector_a or vector == vector_b:
                for v in range(len(vector_list)):
                    if vector_list[v] == vector_a or vector_list[v] == vector_b:
                        del vector_list[v]
                        break
                for v in range(len(vector_list)):
                    if vector_list[v] == vector_a or vector_list[v] == vector_b:
                        del vector_list[v]
                        break
    elif element == 'Знак частицы':
        print(choice(['минус', 'плюс']))
print()
print(f'Найти: {elements_list[0]}')
