""""
Задание №1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.

"""
class Matrix:

    def __init__(self, list_1, list_2):
        self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


my_matrix = Matrix(
    [[7, 5, 3],
     [6, 11, 44],
     [35, 78, 14]],
    [[56, 12, 8],
     [30, 29, 58],
     [45, 8, 77]])

print(my_matrix.__add__())

""""
Задание №2
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return f"Площадь пальто {self.width / 6.5 + 0.5:.2f}"

    def get_square_s(self):
        return f"Площадь костюма {self.height * 2 + 0.3:.2f}"

    @property
    def get_sq_full(self):
        return f"Суммарная расход ткани {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}"


class Coat(Cloth):
    def get_square_c(self):
        return self.width / 6.5 + 0.5


class Suit(Cloth):
    def get_square_j(self):
        return self.height * 2 + 0.3

textil = Cloth(52, 7)
print(textil.get_square_c())
print(textil.get_square_s())
print(textil.get_sq_full)

"""
Задание №2 Не смог реализовать абстрактный класс. НЕ понимаю почему не получается

"""

from abc import ABC, abstractmethod


class Cloth(ABC):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_square_c(self):
        return f"{self.width / 6.5 + 0.5:.2f}"

    @abstractmethod
    def get_square_s(self):
        return f"{self.height * 2 + 0.3:.2f}"

    @property
    def get_sq_full(self):
        return f"Суммарнай расход ткани {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}"


class Coat(Cloth):
    def get_square_c(self):
        return f"Площадь пальто "


class Suit(Cloth):
    def get_square_s(self):
        return f"Площадь костюма "

""""
Задание №3
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.

"""


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f"Результат операции {self.quantity * '*'}"

    def __add__(self, other):

        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return f"Результат операции {(self.quantity - other.quantity) * '*'}" \
            if (self.quantity - other.quantity) > 0 else print("Отрицательно!")

    def __mul__(self, other):
        self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        self.result = Cell(round(self.quantity // other.quantity))
        return Cell(round(self.quantity / other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f"{'*' * cells_in_row} \\n"
        row += f"{'*' * (self.quantity % cells_in_row)}"
        return row


cells1 = Cell(12)
cells2 = Cell(15)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(12))
print(cells1.make_order(5))
print(cells1 / cells2)