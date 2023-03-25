# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# import random as rnd
#
# input_first_list_len = int(input("Введите длину первого списка: "))
# first_list = [rnd.randint(-50, 50) for _ in range(input_first_list_len + 1)]
# print(f"List: {first_list}")
# first_set = set(first_list)
# print(f"Set: {first_set}")
# input_second_list_len = int(input("Введите длину второго списка: "))
# second_list = [rnd.randint(-50, 50) for _ in range(input_second_list_len + 1)]
# print(f"List: {second_list}")
# second_set = set(second_list)
# print(f"Set: {second_set}")
#
# output_list = list(first_set & second_set)
# output_list.sort()
# print("\n")
# for i in output_list:
#     print(i, end=" ")



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random as rnd

num_bushes = int(input("Введите общее количество кустов на грядке: "))
num_berries_bushes = [rnd.randint(1, 50) for _ in range(num_bushes)]
print(num_berries_bushes)
max_berries_in_bushes = 0
num_bush = num_berries_bushes[0]

for i in range(len(num_berries_bushes)):
    if i == len(num_berries_bushes) - 1:
        tmp_max = num_berries_bushes[-2] + \
              num_berries_bushes[-1] + num_berries_bushes[0]
    else:
        tmp_max = num_berries_bushes[i - 1] + \
                  num_berries_bushes[i] + num_berries_bushes[i + 1]
    if tmp_max > max_berries_in_bushes:
        max_berries_in_bushes = tmp_max
        num_bush = i
print(f"Максимальное количество ягод, которое можно собрать равно: {max_berries_in_bushes}")
print(f"Для этого нужно стоять у {num_bush + 1} куста")



