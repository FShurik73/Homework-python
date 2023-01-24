from import_data import import_data
from export_data import export_data
from print_data import print_data
from searsh_data import searsh_data

def greeting():
    print("Вы начинаете использование телефонного справочника.")

def input_data():
    surname = input("Введите фамилию:> ")
    name = input("Введите имя:> ")
    patronymic = input("Введите отчество:> ")
    data_of_birth = input("Введите дату рождения:> ")
    contact_number = input("Введите номер контакта:> ")
    coment = input("Введите коментарий:> ")
    return [surname, name, patronymic, data_of_birth, contact_number, coment] 

def sep_selection():
    sep = input("Введите разделитель:> ")
    if sep == "":
        sep = None
    return sep

def choice_to_do():
    print("Доступные  операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    digit = input("Введите цифру:> ")
    if digit == '1':
        sep = sep_selection()
        import_data(input_data(), sep)
    elif digit == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска:> ")
        data = export_data()
        item = searsh_data(word, data)
        print_data(data)
        if item != None:
            print("Фамилия ".center(20), "Имя ".center(20), "Отчество ".center(20), "Дата рождения ".center(20), "Телефон ".center(15), "Коментарий ".center(30))
            print('-' * 130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данные не обнаружены.")