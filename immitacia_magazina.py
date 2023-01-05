import copy

products = {
    'ball': 9,
    'pen': 3,
    'spoon': 8
}
products1 = copy.deepcopy(products)
# consumer = copy.deepcopy(consumer1)
a = sum(consumer)
try:
    for k,v in products.items():
        # print(k)

        while len(products) >= 0:# and a >= v

            print(f'В магазине остались следующие товары {products}')
            a = sum(consumer)
            print(f'У вас {a} денег')
            if a < int(v):
                print("У вас недостаточно денег купить следующий товар")
                break
            vvod = str(input('Введите какой товар вы хотите купить'))

            for k,v in products1.items():##Obhodim oshibku: RuntimeError: dictionary changed size during iteration
                if vvod == k:

                    z = v##Nashli suumu, kotoruu budem vichitat iz spiska pokupatelya
                    ###Func vozvr novii spisok  monet consumer i novii spisok monet shop:

                    zaplatili = []
                    index = len(consumer)-1
                    print(f'index = {index}')
                    for i in range(len(consumer)):
                        while z >= 0 :#Poka summa k oplate ne stanet menshe 0
                            # print('smth2')
                            # if consumer[index] > z:#Dvigaem index esli poslednyaya denuzhka pokupatelya bolshe
                            #
                            #     index -= 1
                            # if index == 0 and z > consumer[index]:
                            #     print('Денег не осталось')
                            #     break

                            z = z - consumer[index]#Umenshaem neobhodimu dlya oplati summu na poslednuu monetku pokupatelya
                            zaplatili.append(consumer[index])
                            del consumer[index]
                            del consumer1[index]##consumer1 nuzhen chtobi potom sortironut i vsegda bil bi otsortirovan consumer
                            # print(consumer)
                            # print(z)

                            # print('consumer= ', consumer)
                            # consumer = copy.deepcopy(consumer1)
                            index -= 1
                    print(f'Вы заплатили {zaplatili}')
                    del products[k]
                    # print('consumer', consumer)
                    # print('consumer1', consumer1)
                    # products.pop(k)
                    # print(products)
                    sdacha = [] #
                    index = len(shop) - 1
                    while z < 0:

                        if shop[index] > abs(z) and len(shop)!=1:#or
                            index -= 1##Dvigaem index do teh por poka sdacha ne stanet ravna posledney monetke
                            # print('z = ', z, 'dvigaem index ' , index, 'shop index ', shop[index])#z = z + shop[index]
                        elif shop[index] == abs(z):
                            consumer1 = consumer
                            # print('consumer', consumer, 'z = ', z)
                            # print('consumer1', consumer1)
                            z = z + shop[index]
                            # print('z= ', z)
                            sdacha.append(shop[index])

                            consumer1.append(shop[index])
                            consumer = sorted(consumer1)
                            del shop[index]
                            # print(z)
                            # print(shop)
                            print(f'Ваша сдача {sdacha}')
                            # print('consumer' , consumer)
                            # print('consumer1', consumer1)
except RuntimeError as e:
    print('Nothin gona stop us now')