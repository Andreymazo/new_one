####### Собираем в словарь хэши и нехэши###########
# def get_hashes_and_mentions(text):
#
#     hesh_lst = []
#     d = []
#     a = text.split(' ')
#     for i in a:
#         if i[0] == '#':
#             hesh_lst.append(i)
#             # print(c)
#         elif i[0] != '*':
#             d.append(i)
#     print(d)
#     print(hesh_lst)
#     b = {}
#     b.setdefault('hashes', hesh_lst)
#     b.setdefault("mentions", d)
#     print(b)
#
#
#     return {"hashes": ..., "mentions": ...}
#
# get_hashes_and_mentions("Котята #еда @Вася море #лоск")
###########################################Собираем хэши из текста
# def get_hash(text):
#     hesh_lst = []
#
#     text = text.split(' ')
#     for i in text:
#         if i[0] == '#':
#             hesh_lst.append(i)
#     print(hesh_lst)
#
# get_hash("Котята #еда #закат море")# вернет [”#еда”, “#закат”] )
####################### Получает сумму и уровень скидки, возвращает цену с плавающей точкой
# def get_price_with_discount(price, level):
#     dic = {
#         1: 10,
#
#         2: 25,
#
#         3: 50
#     }
#     for k,v in dic.items():
#         if k == level:
#             return  f' {float(price - price*v/100)}'
#
# print(get_price_with_discount(1000, 1))#возвращает 900.0
# print(get_price_with_discount(500, 3))# возвращает 250.0
################################получает сумму и уровень скидок и возвращает цену с плавающей точкой########
# def get_price_with_discount(price, percentage):
#
#         return f'{price - price*percentage/100}'
#
# print(get_price_with_discount(1000, 10))
# # get_price_with_discount(1000, 10)` возвращает 900.0
# #
# print(get_price_with_discount(500, 50))#` возвращает 250.0
##############################################Получает сумму, возвращает скидку - целое число###############
def get_discount(summ):
    dic = {
        1: range(0, 5000),

        2: range(5000, 10000),

        3: range(10000, 20000),

        4: range(20000, 35000),

        5: range(35000, 50000),

        6: range(50000, 10000000)
    }
    for k,v in dic.items():
        if summ in v:
            return k
print(get_discount(7000))
###############################принимает время в секундах, возвращает словарь в формате {”min”: мин, “sec”: сек)}

def get_min_sec(sec):
    m = sec//60
    s = sec%60
    return {f'”min”: {m} мин, “sec”: {s} сек)'}

print(get_min_sec(120))
# `get_min_sec(120)` Вернет `{”min”:2, “sec”:0}`
print(get_min_sec(150))#` Вернет `{”min”:2, “sec”:30}`
print(get_min_sec(15))#` Вернет `{”min”:, “sec”:15}`
################################################Принимает копейки возвращает целые рубли
def get_rur_kop(value):
    rub = int(value/100)
    return f'{rub}'
print(get_rur_kop(230))
print(get_rur_kop(230))#` вернет 2

print(get_rur_kop(590))#` вернет 5
