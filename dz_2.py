# Задание №1

result_list = [2, 'text', 45.3, None, complex(7, 8), bin(17), oct(22), hex(120), [1, 2, 3], ("один", 6), {"a", "b"}]
for el in result_list:
    print(type(el), end=" ")

# Задание №2

num_inter = int(input("Введите количество элементов: "))
my_list = []
index = 0
num_element = 0
while index < num_inter:
    my_list.append(input("Введите значение: "))
    index += 1
print(my_list)
for elem in range(int(len(my_list)/2)):
    my_list[num_element], my_list[num_element+1] = my_list[num_element + 1], my_list[num_element]
    num_element += 2
print(my_list)

# Задание №3

time_of_year_list = ["зима", "весна", "лето", "осень"]
time_of_year_dict = {1 : "зима", 2 : "весна", 3 : "лето", 4 : "осень"}
month = int(input("Введите номер месяца в виде целова числа:"))
if month == 1 or month == 2 or month == 12:
    print(time_of_year_list[0])
    print(time_of_year_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(time_of_year_list[1])
    print(time_of_year_dict.get(2))
elif month == 6 or month == 7 or month ==8:
    print(time_of_year_list[2])
    print(time_of_year_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(time_of_year_list[3])
    print(time_of_year_dict.get(4))
else:
    print("Такого времени года нет")

# Задание №4

str_inter = input("Введите строку из нескольких слов: ")
str_word = []
num = 1
for el in range(str_inter.count(" ") + 1):
    str_word = str_inter.split()
    if len(str(str_word)) <= 10:
        print(f" {num} {str_word [el]}")
        num +=1
    else:
        print(f" {num} {str_word [el] [0:10]}")
        num +=1

# Задание №5

my_list = [9, 5, 3, 3, 2, 1]
print("Рейтинг составляет: ", my_list)
my_number = int(input("Введите число: "))
for el in range(len(my_list)):
    if my_list[el] == my_number:
         my_list.insert(el + 1, my_number)
         break
    elif my_list[0] < my_number:
        my_list.insert(0, my_number)
    elif my_list[-1] > my_number:
        my_list.append(my_number)
    elif my_list[el] > my_number and my_list[el + 1] < my_number:
        my_list.insert(el + 1, my_number)
print("Текущий рейтинг составляет: ", my_list)


























