Введение:
Для облегчения работы склада жидкостей, мы создали каркас класса жидкости,
который необходимо доработать. Вся доработка будет состоять из 4 шагов. Поэтому
каждое задание нужно доделывать до конца по требованию, иначе следующие
шаги не будет возможности реализовать в полной мере. Это первый шаг, в котором
необходимо сделать свое задание, его описание можно найти ниже. Так будет для каждого
шага. Внимательно читайте задание и сначала обсуждайте решение в команде, а
потом беритесь за реализацию.
Условие:
Результат выполнения принимается через репозиторий, в котором хранится решение
всей команды, а не одного человека. При этом в работе необходимо создавать отдельную
ветку для каждой задачи у каждого члена команды, кто загружает свой код. Сливать
результат необходимо через функционал Pull requests.
---
Задание:
В данном шаге реализации необходимо реализовать функциональности для полноценной
работы представленного кода в блоке обработки входной точки в программу, а
также отображения объекта и его инициализации.
"""


class Liquid:
    id: int  # номер жижи, реализовать автоинкремент
    title: str  # название
    density: float  # плотность
    ID = 0

    def __init__(self, title, density, can_drink=True):
        self.title = title
        self.density = density
        Liquid.ID += 1
        self.id = Liquid.ID
        self.can_drink = can_drink


    def __str__(self):
        """
        Реализовать вывод в следующем виде, для жидкости с id=1, названием Воды и плотностью 1000кг/м3:
        1. Жидкость "Вода" с плотностью 1000 кг/м3
        """
        return f'{self.id}. Жидвкость "{self.title}" с плотностью {self.density} кг/м3'



    def __eq__(self, other):
        return self.density == other.density

    def __ne__(self, other):
        return self.density != other.density

    def __lt__(self, other):
        return self.density < other.density

    def __le__(self, other):
        return self.density <= other.density

    def __gt__(self, other):
        return self.density > other.density

    def __ge__(self, other):
        return self.density >= other.density


def sorting(sorting_list):
       """
       Функция сортировки по плотности жидкости, важно
       тут сравнивать именно объекты, а не их свойства, также
       добавить группировку по типу жидкости: питьевая или техническая
       """
       result = sorted(sorting_list)
       return result

class Eatable(Liquid):

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак вкуса """
        return f'{self.id}. Жидвкость "{self.title}" с плотностью {self.density} кг/м3.- можно пить'


class Technical(Liquid):

    def __str__(self):
        """ Добавить уточнение, можно пить или нет и вывести признак вкуса """
        return f'{self.id}. Жидвкость "{self.title}" с плотностью {self.density} кг/м3.- нельзя пить'



if __name__ == '__main__':
    liquid_list = list()
    while True:
        print('Предлагаю вам ввести параметры жидкости')
        title = input('Введите название: ')
        density = input('Введите плотность: ')
        type_of_liquid = input('Это можно пить? [Y/n]: ').upper()
        if type_of_liquid == 'Y':
            new_item = Eatable(title, density)
        else:
            new_item = Technical(title, density)
        liquid_list.append(new_item)



        liquid_list = sorting(liquid_list)
        for i in liquid_list:
            print(i)