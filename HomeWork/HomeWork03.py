# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

import time

input_list = []
input_list_len = int(input("Введите длину массива: "))
for i in range(input_list_len):
    input_list.append(int(input(f"Введите {i + 1} число: ")))
print(input_list)

input_x = int(input("Введите искомое число: "))
start = time.perf_counter()
print(input_list.count(input_x))
end = time.perf_counter()
first_time = end - start

start = time.perf_counter()
count = 0
for i in range(input_list_len):
    if input_list[i] == input_x:
        count += 1
print(count)
end = time.perf_counter()
second_time = end - start

print(f"Скорость выполнения первого алгоритма равна: {first_time}")
print(f"Скорость выполнения второго алгоритма равна: {second_time}")

print(first_time / second_time)


# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

input_list = []
input_list_len = int(input("Введите длину массива: "))
for i in range(input_list_len):
    input_list.append(int(input(f"Введите {i + 1} число: ")))
print(input_list)

input_x = int(input("Введите искомое число: "))
if input_list.count(input_x) > 0:
    print(f"Искомое число {input_x} есть в массиве")
else:
    print(f"Ближайшее число к искомому равно: {min(input_list, key=lambda x: abs(x-input_x))}")



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
#
# ноутбук
#     12

some_dict_en = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
some_dict_ru = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

input_text = input("Введите слово: ").upper()
if len([a for i in input_text for a, b in some_dict_ru.items() if i in b]) == 0:
    print(f"Ценность слова: {sum([a for i in input_text for a, b in some_dict_en.items() if i in b])}")
else:
    print(f"Ценность слова: {sum([a for i in input_text for a, b in some_dict_ru.items() if i in b])}")




