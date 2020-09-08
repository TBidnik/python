# Задание №1

from sys import argv
hours_worked_out, rate_for_the_time, prize = argv
hours_worked_out = int(hours_worked_out)
rate_for_the_time = int(rate_for_the_time)
prize = int(prize)
result = int(hours_worked_out * rate_for_the_time + prize)
print(f"Зраработная плата сотрудника составит - {result}")

# Задание №2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
num = 0
for num, el in enumerate(my_list):
    if my_list[num - 1] < my_list[num]:
        new_list.append(el)
        num += 1
print(new_list)

# Задание №3

print(f"Результат -  {[el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]}")

# Задание №4


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_list = []

for el in my_list:
    if my_list.count(el) < 2:
        new_list.append(el)

print(new_list)

# Задание №5

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el

my_list = range(100, 1001)
new_list = []
for el in my_list:
    if el % 2 == 0:
        new_list.append(el)
print(new_list)
print(f"Результат умножения - {reduce(my_func, new_list)}")

# Задание №6


from itertools import count, cycle
el_count = int(input("Введите целое число с которого начнется итерация: "))
el_count_end = int(input("Введите целое число, до которого будет идти итерация: "))
for el in count(el_count):
    if el > el_count_end:
        break
    else:
        print(el)
el_cycle = input("Введите данные для вывода повторений на экран: ")
print(el_cycle)
el_cycle_num = 1
for el in cycle(el_cycle):
    if el_cycle_num > 9:
        break
    else:
        print(el_cycle)
    el_cycle_num += 1

# Задание №7

from itertools import count
from math import factorial as fact

def my_func():
    for el in count(0, 1):
        yield fact(el)

generate = my_func()
x = 0
n = int(input("До какого значения будем генерировать? :"))
for i in generate:
    if x < n:
        print(i)
        x += 1
    else:
        break
