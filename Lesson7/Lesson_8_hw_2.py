""""
Задание №1
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-" : my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f"Все верно"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"

    def __str__(self):
        return f"Текущая дата {Data.extract(self.day_month_year)}"


today = Data("23 - 9 - 2020")
print(today)
print(Data.valid(13, 8, 2022))
print(today.valid(12, 7, 2011))
print(Data.extract("13 - 8 - 2011"))
print(today.extract("13 - 8 - 2020"))
print(Data.valid(9, 1, 2005))

""""
Задание №2
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

""""
Задание №3
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный
список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить
его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
(не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

"""

class List_digit:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input("Введите значения и нажимайте Enter - "))
                self.my_list.append(val)
                print(f"Текущий список - {self.my_list} \n ")
            except:
                print(f"Недопустимое значение - введите число")
                y_or_n = input(f"Попробовать еще раз? Y/N ")

                if y_or_n == "Y" or y_or_n == "y":
                    print(try_except.my_input())
                elif y_or_n == "N" or y_or_n == "n":
                    return f"Программа завершина"
                else:
                    return f"Программа завершина"

try_except = List_digit(1)
print(try_except.my_input())

""""
Задание №4
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

"""

class Warehouse_Org:
    def __init__(self, name, price, quantity, number, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number = number
        self.my_list_1 = []
        self.my_list_2 = []
        self.my_dictionary = {"Устройство": self.name, "Цена": self.price, "Количество": self.quantity}

    def __str__(self):
        return f"Устройство {self.name} Цена {self.price} Количество {self.quantity}"

    def data_entry(self):
        try:
            unit_name = input("Введите наименование")
            unit_price = input("Введите цену")
            unit_quantity = input("Введите количество")
            unit_dictionary = {"Наименование": unit_name, "Цена": unit_price, "Количество": unit_quantity}
            self.my_dictionary.update(unit_dictionary)
            self.my_list_2.append(self.my_dictionary)
            print(f"Текущий список -\n {self.my_list_2}")
        except:
            return f"Данные введены не верно!"

        print(f"Для выхода нажмите - Q, для продолжения нажмите - Enter")
        q = input("  ")
        if q == "Q" or q == "q":
            self.my_list_1.append(self.my_list_2)
            print(f"Полный список склада -\n {self.my_list_1}")
        else:
            return Warehouse_Org.data_entry(self)


class Printer(Warehouse_Org):
    def to_print(self):
        return f"{self.number}"

class Scan(Warehouse_Org):
    def to_scan(self):
        return f"{self.number}"

class Copy_Machine(Warehouse_Org):
    def to_copy(self):
        return f"{self.number}"

class Computer(Warehouse_Org):
    def to_computer(self):
        return f"{self.number}"
unit_1 = Printer("HP", 2000, 5, 10)
print(unit_1.my_dictionary)
unit_2 = Scan("CANNON", 1500, 3, 15)
print(unit_2.my_dictionary)

""""
Задание №5
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f"Сумма z1 и z2 равна")
        return complex(self.a + other.a) + complex(self.b + other.b)

    def __mul__(self, other):
        print(f"Произведение z1 и z2 равно")
        return complex(self.a * other.a - self.b * other.b) + (self.b * other.a + self.a * other.b)


z_1 = ComplexNumber(7, -9j)
z_2 = ComplexNumber(3, 4j)
print(z_1 + z_2)
print(z_1 * z_2)