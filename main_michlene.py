import os
import shutil
import time
from datetime import datetime
from tqdm import tqdm
import sort_mal_files
from sort_mal_files import sort_mal_fil


def rm_r(path):
    print("Udaliaem ...")
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

import csv
def zapis(data_,file_counter_):
    with open(f'{filepath_1}/newfile_{file_counter_}.csv', 'w+') as ff:#, newline=''
        # writer = csv.writer(ff)#Для записи данных есть функция 'writer()' Нам не подошла почему-то
        # writer.writerow(i)
        ff.writelines(data_)

def devider():
    line_counter = 0
    file_counter = 0

    with open('michelin_data.csv') as f:
        header = next(f)
        data = [header]  # Поставили курсор на оглавление

        for i in tqdm(f):#61923531it [01:20, 765607.25it/s]
            #time.sleep(0.1) с тайм слипом не получится
            if line_counter >= 100000:
                line_counter = 0
                file_counter += 1
                zapis(data, file_counter)
                # print("Here we are")
                data = [header]
            data.append(i)
            line_counter += 1
        file_counter += 1
        # file_counter += 1  # Дозаписываем остаток в 8ой файл
        if len(data) > 0:

            with open(f'{filepath_1}/newfile_{file_counter}.csv', 'w+', newline='') as ff:
                ff.writelines(
                    data)  #######Здесь у нас поделенный файл на несколько. Дальше соберем в один и походу сортируем
    return file_counter


if __name__ == "__main__":
    filepath_1 = 'temp1'
    filepath_2 = 'result_dir'
    filepath_3 = 'result_dir_result'

    if os.path.isdir(filepath_1):## Создали три дериктория для первичных файлов, для результирующих отсортированных и совсем собранных результирующих
        print('Есть директория: temp1')
    else:
        os.mkdir(filepath_1)
    if os.path.isdir(filepath_2):
        print('Есть директория: result_dir')
    else:
        os.mkdir(filepath_2)
    if os.path.isdir(filepath_3):
        print('Est diretoria result_dir_result')
    else:
        os.mkdir(filepath_3)

    g = len(os.listdir(filepath_1))
    gg = len(os.listdir(filepath_2))
    devider()#Эта функция нашинкует 620 файлов по 100 000 строчек в каждом

    print(f'В папке temp1: {g} в папке result_dir: {gg}')
    sort_mal_files.sort_mal_fil(filepath_1,filepath_2)#Эта функция отсортирует 620 файлов и перезапишет их по 100 000 строчек в каждом
    #У нас 620 отсортированных файлов, пробежимся по ним и выберем 10 топ продаж с каждого ,соберем в один файл result_file2 6200 строчек
    sort_mal_files.vibiraem_max_kol()
    ########### vibiraem_max_kol()# Получили 6200 значений в файле result_file2
    sort_mal_files.sort_videl_unik()
    # ##########Выделим из файла result_file3 3 максимальных значения, для этого отсортируем его и выведем 3 первые значения
    sort_mal_files.vived_()

    ff = int(input('Если все проверили, то можно удалять все файлы и папки? Нажмите 1 Если еще хотите посмотреть, то хм.. смотрите'))


    if ff == 1:
        rm_r(filepath_1)
        rm_r(filepath_2)
        rm_r(filepath_3)
