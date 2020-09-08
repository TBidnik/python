# Задание №1

def num_calc(*args):
    try:
        first_num_calc = int(input("Введите первое число: "))
        second_num_calc = int(input("Введите второе число: "))
        num_val = first_num_calc / second_num_calc
        if second_num_calc != 0:
            return first_num_calc / second_num_calc
        else:
            print("Введите корректное значение. На ноль делить нельзя!!!")
        return num_val
    except ValueError:
        return "Ошибка"
    except ZeroDivisionError:
        return "Неверное значение. Вы не можете использовать ноль в качестве значения"

print(f'Результат равен =   {num_calc()}')

# Задание№2

def data_func(*args):
    name = input("Введите ваше имя:")
    surname = input("Введите вашу фамилию:")
    year = input("Введите ваш год рождения:")
    city = input("Введите ваш город проживания:")
    email = input("Введите ваш email:")
    telephone = input("Введите ваш телефон:")
    data_new = str(f"Имя - {name}; Фамилия - {surname}; Год рождения - {year}; Город проживания - {city}; Email - {email}; Телефон - {telephone}")
    return data_new
print(data_func())


# Задание№3
def my_func(*args):
    el_1 = input("Введите первое число:")
    el_2 = input("Введите второе число:")
    el_3 = input("Введите третье число:")
    el_new = [el_1, el_2, el_3]
    el_new.remove(min(el_1, el_2, el_3))
    return sum(el_new)


summa = my_func()
print(int(summa))


# Задание№4

def my_func(x, y):
    return 1 / x ** abs(y)
def my_func_use():
    print(my_func(2, -2))
def my_func_2(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x
def my_func_2_use():
    print(my_func(2, -2))


# Задание №5

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите список чисел через пробел или нажмите Q для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма равна {sum_res}')
    print(f'Итоговая сумма равна {sum_res}')


my_sum()



# Задание №6

def int_func (*args):
    word = input("Введите фразу ")
    print(word.title())
    return
int_func()