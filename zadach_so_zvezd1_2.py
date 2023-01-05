# ####################Zadacha 1###################
a = str(input("Привет! Предлагаю проверить свои знания английского!"
      "Расскажи, как тебя зовут!"))
print(f'Привет, {a}, начинаем тренировку!')


def proverka_vop():
    vopros = {
        'My name ___ Vova': 'is',
        'I ___ a coder': 'am',
        'I live ___ Moscow': 'in'
    }
    counter = 0
    counter_vop = 0
    for i, ii in vopros.items():
        aa = input(f'Вопрос : {i}')
        if aa == ii:
            print('Ответ верный!')
            print('Вы получаете 10 баллов!')
            counter += 10
            counter_vop += 1
        if aa != ii:
            print('Неправильно')
            print(f'Правильный ответ: {ii}')
    print(f'Вот и все, {a}!')
    print(f'Вы ответили на {counter_vop} вопросов из 3 верно.')
    print(f'`Вы заработали {counter} баллов.Это {counter * 33 / 10} процентов.')


proverka_vop()
########################Печатаем 2 на 4 звездочками (Перекопировал задачу ниже, она такая же, только  с переменными)
# def print_square(x, y):
#     a = ''
#     for i in range(0,x):
#         a += '*'
#     print(a)
#     for i in range(0,y-1):
#         print(a)
#
#
# print_square(3, 4)
##########################Печатаем строчку длиной x
# def print_line(x):
#     a = ''
#     for i in range(0,x):
#         a += '*'
#     print(a)
# print_line(7)
#########################Печатаем прямоугольник со сторонами x,y
# def print_square(x, y):
#     a = ''
#     for i in range(0,x):
#         a += '*'
#     print(a)
#     for i in range(0,y-1):
#         print(a)
#
#
# print_square(3, 4)
######################Перевод оценки 2-5 в хорошо и тп.

# def get_grade(grade):
#     dic = {
#     'Плохо': 2,
#     'Удовлетворительно': 3,
#     'Хорошо': 4,
#     'Отлично': 5
#     }
#     for k,v in dic.items():
#         if grade == v:
#             print(k)
# get_grade(3)

############################Площадь кружочка
# import math
# def get_square(radius):
#     # print(math.pi)
#     s = radius ** 2 * math.pi
#     print(s)
# get_square(2)
######################Часы выводим период и время суток

# def get_period(hour):
#     s1 = set(int(i) for i in range(0, 6))
#     s2 = {int(i) for i in range(7, 11)}
#     s3 = set(int(i) for i in range(12, 17))
#     # s4 = set(int(i) for i in range(18, 24))
#     # print(s2)
#     dic = {
#     '0-6 - ночь': s1,
#     '7-11 - утро': s2,
#     '12-17 - день': s3,
#     '18-24 - вечер': range(18, 24)#Можно без множеств, тоже пойдет
#     }
#     for k,v in dic.items():
#         if hour in v:
#             print(f'{k}')
# get_period(5)

###################Баллы в оценку###############
# def get_grade(x):
#     v1 = set(int(x) for x in range(0, 40))
#     v2 = set(int(x) for x in range(40, 60))
#     v3 = set(int(x) for x in range(60, 80))
#     v4 = set(int(x) for x in range(80, 101))
#     print(v4)
#     dic = {
#     'Плохо': v1,
#     'Удовлетворительно': v2,
#     'Хорошо': v3,
#     'Отлично': v4
#     }#range(81 - 100)range(61 - 80)
#     for k,v in dic.items():
#         if int(x) in v:
#             print(k)
# get_grade(80)
############################Среднеарифметич округленное до целого числа###############
# def avg(items):
#     counter = 0
#     total_sum = 0
#     for i in items:
#         total_sum += i
#         counter += 1
#     avg_sum = total_sum/counter
#     print(round(avg_sum))
# avg([3, 5, 7, 1, 3])
################Кортавость
# def has_rrr(word):
#     a = 'р'
#     if a in word:
#         return True
#     return False
# print(has_rrr('речка'))
#####################Самое длинное слово
# def the_longest(words):
#     index = 0
#     word = ''
#     for i in range(len(words)-1):
#         print(len(words[index]))
#         if len(words[index]) >= len(words[index+1]):
#             word = words[index]
#         word = words[index+1]
#         index += 1
#     print(word)
# the_longest(["еж" , "вещь", "стриж"])