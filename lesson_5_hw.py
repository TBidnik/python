""""
# Задание №1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


my_file = open('lesson_5_hw_1.txt', 'w')
text_1 = input('Введите текст \n')
while text_1:
    my_file.writelines(text_1)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
with open('lesson_5_hw_1.txt') as f_obj:
    for line in f_obj:
        print(line)

""""
# Задание №2
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

out_f = open("lesson_5_hw_2.txt", "w")
str_list = ["stroka_1\n", "Hello World\n", "Galaxy\n"]
out_f.writelines(str_list)
out_f.close()
with open("lesson_5_hw_2.txt") as f_obj:
    for line in f_obj:
        print(line)
my_file = open("lesson_5_hw_2.txt", "r")
content = my_file.readlines()
print(f"Количество строк в файле - {len(content)}")
for i in range(len(content)):
    print(f"Количество символов {i + 1} строки {len(content[i])}")
my_file = open("lesson_5_hw_2.txt", "r")
content = my_file.read()
content = content.split()
print(f"Общее количество слов - {len(content)}")
my_file.close()


""""
# Задание №3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
 их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., 
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""

incomes = []

with open("lesson_5_hw_3.txt", "r",  encoding='utf-8') as my_file:
    lines = my_file.readlines()

    for line in lines:
        name, income = line.split()
        income = int(income)
        incomes.append(income)
        if income < 20000:
            print(name)
    print(sum(incomes) / len(incomes))


""""
# Задание №4
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен
 записываться в новый текстовый файл.
"""

out_f = open('lesson_5_hw_4_1.txt', 'w')
str_list = ["One - 1 \n", "Two - 2\n", "Three - 3\n", "Four - 4\n"]
out_f.writelines(str_list)
out_f.close()
with open('lesson_5_hw_4_1.txt') as f_obj:
    for line in f_obj:
        print(line)
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('lesson_5_hw_4_1.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('lesson_5_hw_4_2.txt', 'w',  encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)

""""
# Задание №5
Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""

def summary():

    with open('lesson_5_hw_5.txt', 'w') as file_obj:
        line = input('Введите цифры через пробел \n')
        file_obj.writelines(line)
        my_num = line.split()

        print(sum(map(int, my_num)))
summary()

""""
# Задание №6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:       100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""

my_dict = {}
with open("lesson_5_hw_6.txt") as t_obj:
    for line in t_obj:
        name, stats = line.split(":")
        name_sum = sum(map(int, "".join([i for i in stats if i == " " or i.isdigit()]).split()))
        my_dict[name] = name_sum
print(my_dict)

with open("lesson_5_hw_6.txt", "r") as t_obj:
    lines = t_obj.readlines()
    for line in lines:
        new_str = "".join((i if i in "1234567890" else " ") for i in line)
        new_2 = [int(i) for i in new_str.split()]
        print(f"{line.split()[0]} {sum(new_2)}")

""""
# Задание №7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка 
должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, также добавить 
ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.


"""

import json

with open("lesson_5_hw_77.json", "w") as j_file:
    with open("lesson_5_hw_7.txt", "r") as f_o:
        subjects = {}
        middle = {}
        k, o = 0, 0
        line = f_o.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            subjects[i[0]] = profit
            if profit > 0:
                k += profit
                o += 1
            middle["avegare"] = k / o
        all_list = [subjects, middle]
    json.dump(all_list, j_file)

