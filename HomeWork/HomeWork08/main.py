import function


while True:
    print("1. Вывод, 2. Добавление, 3. Поиск, 4. Удалить, 5. Изменение")
    mode = int(input())
    if mode == 1:
        function.show_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    elif mode == 4:
        function.del_data()
    elif mode == 5:
        function.change_data()
    else:
        break

# ФИО | Номер телефона
# ФИО1 | Номер телефона1
# шаров сергей юрьевич | 89288478468
# аааа | 4234324324
# фывфыв сергей аываыв | 4234324
# сергей | 4234234
# авыавы | 4234324
