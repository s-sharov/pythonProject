# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

path_file = "book.txt"

def show_data() -> None:
    """Выводит информацию из справочника"""
    with open(path_file, "r", encoding="utf-8") as f:
        print("__________________________________________________________")
        print(f.read())
        print("__________________________________________________________")


def add_data() -> None:
    """Добавляет информацию в справочник"""
    input_fio = input("Введите ФИО: ")
    input_tel_number = input("Введите номер телефона: ")
    with open(path_file, "a", encoding="utf-8") as f:
        f.write(f"\n{input_fio} | {input_tel_number}")
    print("Данные успешно добавлены!")


def find_data() -> None:
    """Поиск информации в справочнике"""
    input_find = input("Введите искому информацию в словаре: ")
    with open(path_file, "r", encoding="utf-8") as f:
        tel_book = f.read()
    print("Результат поиска: ")
    print("__________________________________________________________")
    print("Индекс | ФИО | Номер телефона")
    print("\n".join(search(tel_book, input_find)))
    print("__________________________________________________________")


def del_data() -> None:
    """Удаляет запись из справочника"""
    list_tmp = []
    with open(path_file, "r", encoding="utf-8") as f:
        for i, j in enumerate(f.read().split("\n"), start=1):
            print(i, j)
            list_tmp.append(j)
        row_del = int(input("Введите номер строки для удаления: "))
        if row_del < 1 or row_del > len(list_tmp):
            print("нет такой строки")
            return
        list_tmp.pop(row_del - 1)
    print(list_tmp)
    with open(path_file, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(list_tmp))


def change_data():
    """Изменяет информацию в справочнике"""
    list_tmp = []
    with open(path_file, "r", encoding="utf-8") as f:
        for i, j in enumerate(f.read().split("\n"), start=1):
            list_tmp.append(j)
        row_change = int(input("Введите номер строки для изменения: "))
        if row_change < 1 or row_change > len(list_tmp):
            print("Такая строка отсутствует")
            return
        tmp_fio = input("Введите ФИО: ")
        tmp_tel_num = input("Введите номер телефона: ")
        list_tmp[row_change-1] = f"{tmp_fio} | {tmp_tel_num}"
    with open(path_file, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(list_tmp))


def search(book: str, search_str: str) -> list:
    """Находит в строке записи по определенному критерию поиска"""
    book = book.split("\n")
    result = []
    for line in book:
        if search_str in line:
            result.append(line)
    return result

