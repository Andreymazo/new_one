import os
import csv
import time
from datetime import datetime
from itertools import islice
from sort_qwck_sort import quick_sort
from operator import itemgetter
from tqdm import tqdm
# os.remove() removes a file.
#
# os.rmdir() removes an empty directory.
#
# shutil.rmtree() deletes a directory and all its contents.

def sort_mal_fil(filepath_11, filepath_22):
    global vved_nomer
    filepath_11 = 'temp1'
    filepath_22 = 'result_dir'
    g = len(os.listdir(filepath_11))
    global gg
    gg = len(os.listdir(filepath_22))
    print(f'В папке temp1 {g} в папке result_dir {gg}')
####################Probuem bez slovarya###########
# for i in range(1,2):
#     print(f"Sortirovka po high,  file: {i}")
#     with open(f'{filepath}/newfile_{i}.csv', 'r', encoding='utf8') as f:
#         data = csv.DictReader(f, fieldnames=None, delimiter=',')
#         dic = []
#         for i in data:
#             dic.append(i)
##print(dic)##v kazhdoy strochke fieldsnames#####################

#######################################Sortiruem malenkie file#############################
    try:
        vved_nomer = int(
            input('Введите номер по которому сортировать: diameter 0, s 1, cai 2, region 3, last_sale 4, amount 5'))
        #vved_nomer = int(input('Введите номер по которому сортировать: date 0, open 1, high 2, low 3, close 4, volume 5, Name 6'))
    except TypeError or ValueError:
        print('Введите число от 0 до 6')

    for i in tqdm(range(1, g+1)):
        time.sleep(0.3)
        print(f"Сортировка по  {vved_nomer},  файл№: {i}")
        with open(f'{filepath_11}/newfile_{i}.csv', 'r', encoding='utf8') as f:
            data = csv.DictReader(f, fieldnames=None, delimiter=',')
            dicc = {}
            index = 0
            get_columns = itemgetter('diameter', 's', 'cai', 'region', 'last_sale', 'amount')
            #get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')## Ubiraem fieldnames
            for ii in data:#islice(data, 1000):##Perevedem v dict i sortiruem
                dicc[index] = get_columns(ii)  ##V kachestve kluchei znachenia high iz high_lst
                index += 1
            # print(dicc)
            quick_sort(dicc, vved_nomer)
            dic = []
            for k, v in dicc.items():
                dic.append(dicc[k])

            with open(f'{filepath_22}/result_file_{i}.csv', 'w+', newline='') as ff:#Nado dic zapisat v novii file
                # fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
                # result_data = csv.DictWriter(ff, fieldnames=fieldnames)#Tolko chtobi postavit nazvanie kolonok 3 strochki
                # result_data.writeheader()###No dlia sortirovki nam poka ne nado
                writer = csv.writer(ff)#Zanosim v file
                writer.writerows(dic)
# sort_mal_fil('temp1', 'result_dir')
#У нас 620 отсортированных файлов, пробежимся по ним и выберем 10 топ продаж с каждого ,соберем в один файл result_file2 6200 строчек

def vibiraem_max_kol():
    global vved_nomer, data_sell
    filepath_11 = 'temp1'
    filepath_22 = 'result_dir'
    filepath_33 = 'result_dir_result'
    g = len(os.listdir(filepath_11))
    gg = len(os.listdir(filepath_22))
    vvod_limit = int(input('Введите максимальное число по уже отсортированному параметру, например, ... ТОП продаж, если отсортировано по продажам '))
    data_sell_rez = []
    # while len(data_sell_rez) < vvod_limit * 4:  # and data_sell not in data_sell_rez
    for i in tqdm(range(1, gg)):
            time.sleep(0.25)
            with open(f'{filepath_22}/result_file_{i}.csv', 'r', encoding='utf8') as file_i:
                data = csv.reader(file_i, delimiter=',')
                data_ = []
                for ii in data:
                    data_.append(ii)
            data_sell = []

            while len(data_sell) < vvod_limit:#and len(data_sell_rez) <= vvod_limit*3
                m = max(data_, key=lambda e: e[5])
                    # print(m)
                    # lst_indexes = [ii for ii, j in enumerate(data) if j == m]
                    # print(lst_indexes)
                    # print(data)#<_csv.reader object at 0x0000021FDBD42B60>
                    # H = set()
                    # index = 0
                for ii in tqdm(data_):
                    # time.sleep(0.25)
                        # if ii != m:
                        #     index += 1
                        # if ii == m and ii[5] not in H:

                    if ii == m and ii not in data_sell:
                        data_.remove(ii)
                        data_sell.append(ii + ["\n"])  # writelines не переводит на новую строку. приходится добавлять самим когда аппендим

                            # if ii not in data_sell_rez:
                            #     data_sell_rez.extend(data_sell)
                        #         data_sell_rez.append(data_sell[index])
                        #         index += 1
                        # index += 1
            data_sell_rez.extend(data_sell)#, print(data_sell), print(len(data_sell))#data_sell_rez.extend(data_sell), print(data_sell_rez), print(len(data_sell_rez))

        # return data_sell_rez, print('data_sell_rez ', data_sell_rez ), print('data_sell_rez ', len(data_sell_rez))

        # return data_sell_rez, print(data_sell_rez), print(len(data_sell_rez))
            # return data_sell_rez, print(data_sell_rez), print(len(data_sell_rez))
            with open(f'{filepath_33}/result_file2', 'w+', newline='') as resultfile:
                fieldnames = ['diameter', 's', 'cai', 'region', 'last_sale', 'amount']
                result_data = csv.DictWriter(resultfile, fieldnames=fieldnames)  # [*data.fieldnames]
                print(f'Запущен процесс одновременного считывания и записи, файл: {i}')
                for iii in data_sell_rez:
                # print(ii)
                    words = ",".join(iii)
                    resultfile.writelines(words)


# vibiraem_max_kol()
#Функция оказалась бесполезной, так как в предыдущем ходе все 6200 строчек уже уникальные. Зато она отсортировала заодно.
def sort_videl_unik():
    with open('result_dir_result/result_file2', 'r', encoding='utf-8', newline='') as f:
        data = csv.reader(f, delimiter=' ')
        data_ = []
        for i in data:
            i = str(i)
            i = i.replace('\'','')
            i=i[:len(i)-2]+i[len(i)-1:]#Udalili lishnuu zapiatuu - предпоследний элемент
            i = i.split(",")
            print(i)
            data_.append(i)
            # newstr = oldstr[:midlen] + oldstr[midlen + 1:]
            # print(i)
        # [13, 143, 17058645, Georgia, 2022 - 0407, 99996.44, ]
        # [16, 217, 17094279, Georgia, 2022 - 1130, 99996.63, ]
        # [16, 217, 17094279, Georgia, 2022 - 1130, 99996.63]
        # [13, 143, 17058645, Georgia, 2022 - 0407, 99996.44]

        quick_sort(data_, 5)
        # print(data_)

        def dupl(data_2):##Ubiraem duplikati v otsortirovannom spiske data_
            index = 0
            index2 = 0
            data_finish=[]
            while index < len(data_2):
                while index < len(data_2)-1 and data_[index] == data_[index+1]:
                    index += 1
                data_2[index2] = data_2[index]
                data_finish.append(data_2[index2])
                index2 += 1
                index += 1

            return data_finish
            #return print(index2), print(data_finish)6
#[['13', '143', '17058645', 'Georgia', '2022-0407', '99996.44', ''], ['13', '143', '17058645', 'Georgia', '2022-0407', '99996.44', ''], ['13', '143', '17058645', 'Georgia', '2022-0407', '99996.44', ''], ['16', '217', '17094279', 'Georgia', '2022-1130', '99996.63', ''], ['16', '217', '17094279', 'Georgia', '2022-1130', '99996.63', ''], ['16', '217', '17094279', 'Georgia', '2022-1130', '99996.63', '']]

    data_finish = dupl(data_)
    # print(data_finish)

    with open('result_dir_result/result_file3', 'w+', encoding='utf-8', newline='') as f:
        # fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
        # result_data = csv.DictWriter(f, fieldnames=fieldnames)#Tolko chtobi postavit nazvanie kolonok 3 strochki
        # result_data.writeheader()###No dlia sortirovki nam poka ne nado
        writer = csv.writer(f)  # Zanosim v file
        writer.writerows(data_finish)

# sort_videl_unik()


##########Выделим из файла result_file3 3 максимальных значения, для этого отсортируем его и выведем 3 первые значения
def vived_():
    with open('result_dir_result/result_file3', 'r', encoding='utf-8', newline='') as f:
        # data = csv.reader(f, delimiter=' ')
        data_ = []
        for i in f:
            # print(type(i))
            i = i[:len(i) - 2] + i[len(i):]
            i = i.split(',')
            # print(type(i))
            print(i)
            data_.append(i)
        #
        quick_sort(data_, 5)#Lishnyaya sortirovka
        print(data_)
        data_new = []
        index = 0
        for i in data_:
            if index < 10:
                data_new.append(i)
                index += 1
        print(data_new)
        with open('result_dir_result/result_file4', 'w+', encoding='utf-8', newline='') as f:
            fieldnames = ['diameter', 's', 'cai', 'region', 'last_sale', 'amount']
            result_data = csv.DictWriter(f, fieldnames=fieldnames)#Tolko chtobi postavit nazvanie kolonok 3 strochki
            result_data.writeheader()###No dlia sortirovki nam poka ne nado
            writer = csv.writer(f)  # Zanosim v file
            writer.writerows(data_new)

# vived_()



                            # fw.write('\n'.join(line_list) + '\n')
                            # fw.writelines(line + '\n' for line in line_list)
                            # result_data.writerow(words)
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 17, 144, 33648152, Georgia, 2022 - 0421, 99999.22,
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 17, 144, 33648152, Georgia, 2022 - 0421, 99999.22,
                        # 18, 162, 67297917, Georgia, 2022 - 0315, 99999.86,
                        # 17, 144, 33648152, Georgia, 2022 - 0421, 99999.22,

                # return data_sell_rez,

                        # print('index = ', index)
                        ## del (data, m)

                    #
                    #     print('index = ', index)
                    # index += 1
                    # print(ii)
                # print(m) # 1%|          | 6/620 [00:00<00:36, 16.67it/s]['14', '119', '51413422', 'Georgia', '2022-0205', '99996.68']


                # H = []
                # index = 0
                # for ii in data:
                #     if index < vvod_limit and max(data,  key=lambda e: e[5]) not in H:
                #         H.append(max(data, key=lambda e: e[5]))
                #
                #
                # for ii in H:  # Выводим 5 вакансий с максимальными заплатами
                #     print(f"Пять компаний с максимальными зарплатами вакансии Повар:  {ii}")

                # collect = []
                # index = 0
                # for ii in data:
                #
                #     if ii == m:
                #         print("Index = ", index)
                #         collect.append(ii)
                #         del (data, ii)
                #         print("Collect = ", collect)
                #         index += 1
                #     if ii != m:
                #         print('Smth')
                #         index += 1


                #print(m)#2%|▏         | 10/620 [00:00<00:38, 16.04it/s]['13', '150', '85801060', 'Georgia', '2022-0821', '99999.53']

                #
                # #

                #
                # #[9, 12]
                # #max(data, key=)

                # result_data.writeheader()
                # for ii in data:
                #     result_data.writerow(ii)


#################Soberem v odin i otsortituem i ego, sobrat mozhno, no kogda 3Gb razmer, sortirovat ne poluchitsia,
##################### dlya etogo razbivaem na mnogo filov i sortiruem i dalshe rabotaem s kazhdim filom
    # with open(f'{filepath_22}/result_file',
    #           'a', newline='') as resultfile:  ##Vse ravno s nachala pishet, no potom s 400 000 norm, 1 file otdelno zapisat nado
    #     fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
    #     result_data = csv.DictWriter(resultfile, fieldnames=fieldnames)  # [*data.fieldnames]
    #     # file_i = open(f'{filepath}/newfile_{i}.csv', 'r', encoding='utf8')  # Ostalnie otkrivaem s mode 'a', pishet v konec fila
    #     for i in range(1, gg):
    #         print(f'Zapushen process : {i}')
    #         with open(f'{filepath_11}/newfile_{i}.csv', 'r', encoding='utf8') as file_i:
    #             data = csv.DictReader(file_i, delimiter=',')
    #             result_data.writeheader()
    #             for ii in data:
    #                 result_data.writerow(ii)