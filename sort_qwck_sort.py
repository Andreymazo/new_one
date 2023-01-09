import csv
from operator import itemgetter

#
# def dec_cache(func):
#     cache = {}
#
#     def wrapper(dic):
#         if dic[0] in cache:
#             return dic[0]
#         cache[0] = func(cache)
#         return dic[0]
#
#     return wrapper
#
#
# @dec_cache
# def sort_single_file(dic):  ###Минимальное число справа и проверка на отсортированность counter = 0
#     # counter счетчик заменыб если нуль, то отсортирован
#     #####Сначала пробежим и найдем наименьший элемент
#     print(len(dic))
#     result = False
#     while not result:  # Сюда надо снова подать будет список после его сортировки пополам, т.е. high из функции f_3
#         index = 0
#         counter = 0
#         print(counter, index, len(dic))
#         for i in range(len(dic)):
#             try:
#                 # print(high)
#                 # if high[index] < high[index + 1] and index==len(high):
#                 #     index = 0
#                 if dic[index][2] < dic[index + 1][2]:
#                     dic[index][2], dic[index + 1][2] = dic[index + 1][2], dic[index][2]  ###Наименьший элемент в конце цикла окажется на последнем месте
#                     index += 1
#                     counter += 1
#                     print(counter, len(dic))
#                 elif dic[index][2] > high[index + 1][2]:
#                     index += 1
#                 elif dic[index][2] == high[index + 1][2]:
#
#                     index += 1
#                 #     counter += 1
#                 if counter == 0 and index == len(dic) - 1:  ##Услловие выхода из прогграммы, весь список отсортирован, ni odnogo izmenenia ne proizoshlo
#                     print(counter, len(dic))
#                     result = True  ## V etoi tochke dolzhen bit otsortirovannii spisok high i spisok ost s duplicarami
#                     break  # No pochemu to go konca nedosortirovivaet
#
#             except IndexError:
#                 pass
#             continue
#     return dic

import csv
from itertools import islice
from operator import itemgetter
import pprint
# data/temp/{i + 1}

# def dec_cache(func):
#     cache = {}
#     def wrapper(dic):
#         if dic[0] in cache:
#             return cache[0]
#         value = func(dic)
#         cache[0] = value #Value ne nuzhen ne znau pochemu
#         return cache[0]
#     return wrapper
# @dec_cache
def sort_single_file(nums, low, high, nomer):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i][nomer] < pivot[nomer]:
            i += 1

        j -= 1
        while nums[j][nomer] > pivot[nomer]:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums, nomer):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = sort_single_file(items, low, high, nomer)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)