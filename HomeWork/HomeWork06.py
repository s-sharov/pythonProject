
#
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# first_num = int(input("Введите первый элемент: "))
# difference = int(input("Введите разность: "))
# numbers = int(input("Введите количество элементов: "))
#
#
# def arithm_progression(f_n, dif, num):
#     return [i for i in range(f_n, num * dif+1, dif)]
#
#
# print(arithm_progression(first_num, difference, numbers))



from random import randint



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
some_list = [randint(1, 100) for i in range(10)]
spec_min = int(input("Введите минимум: "))
spec_max = int(input("Введите максимум: "))
print(some_list)


def find_indexs(arr: list, n_min, n_max):
    result_list = list()
    for i in range(len(arr)):
        if n_min < arr[i] < n_max:
            result_list.append(i)
    return result_list


print(find_indexs(some_list, spec_min, spec_max))