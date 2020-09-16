""""
Задание №1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
import time
class TrafficLight:
    def __init__(self):
        self.__trafficlight_collor = "color"

    def on_traficlight_running(self, red="", yellow="", green=""):
        print("Светофор включен")
        self.red = "Горит Красный"
        self.yellow = "Горит Желтый"
        self.green = "Горит Зеленый"
a = TrafficLight()
a.on_traficlight_running()
print(a.red)
time.sleep(7)
print(a.yellow)
time.sleep(2)
print(a.green)
time.sleep(1)


""""
Задание №2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого 
для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта 
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. 
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, _length, _width, depth, mass):
        self._length = _length
        self._width = _width
        self.depth = depth
        self.mass = mass

    def square(self):
        return self._length * self._width * self.depth * self.mass // 100


a = Road(20, 500, 25, 5)
print(f"Масса асфальта составит - {a.square()} тонн")


""""
Задание №2 (Если я не правильно понял задание)
"""

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        return self._length * self._width

class Mass(Road):

    def __init__(self, _length, _width, depth, mass):
        super(). __init__(_length, _width)
        self.depth = depth
        self.mass = mass

    def dema(self):
        return self._length * self._width * self.depth * self.mass


a = Mass(20, 500, 25, 5)
print(a.square())

""""
Задание №3
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть 
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

a = Position("Иван", "Добрынин", "WEB - разработчик", 203000, 30000)
print("Полное имя сотрудника:")
print(a.get_full_name())
print("Заработная плата сотрудника с учетом премиальных")
print(a.get_total_income())

""""
Задание №4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.

"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} - Наша машина поехала"
    def stop(self):
        return f"{self.name} - Наша машина остановилась"
    def turn_left(self):
        return f"{self.name} - Наша машина повернула налево"
    def turn_right(self):
        return f"{self.name} - Наша машина повернула направо"
    def show_speed(self):
        return f"Скорость нашей машины {self.name} составляет {self.speed}"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!!!! ")
        else:
            return f"Скорость вашей машины {self.name} нормальная и составляет {self.speed.get}"
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!!!! ")
        else:
            return f"Скорость вашей машины {self.name} нормальная и составляет {self.speed.get}"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(self, speed, color, name)

    def police(self):
        if self.is_police:
            return f"{self.name} Все с дороги!!! Это полиция!!!"

a = TownCar(70, "Чёрный", "Lexsus", False)
b = SportCar(100, "Красный", "Ferrari", False)
c = WorkCar(30, "Зеленый", "Газель", False)
d = PoliceCar(250, "Серый", "Ford", True)
print(a.turn_left())
print(b.go())
print(a.show_speed())
print(d.show_speed())
print(d.police())

""""
Задание №5 
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, 
что выведет описанный метод для каждого экземпляра.

"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Я взял {self.title}. Я рисую ручкой!"

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Я взял карандаш {self.title}. Я рисую карандашом!"

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return  f"Я взял маркер {self.title}. Я рисую маркером!"
pen = Pen("Ручку")
pencil = Pencil("")
handle = Handle("")
print(pen.draw())
print(pencil.draw())
print(handle.draw())