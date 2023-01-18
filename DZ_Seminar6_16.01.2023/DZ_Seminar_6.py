# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

fileName = 'Phonebook.txt'

def pause():
    input('Чтобы вернуться в меню, нажмите Enter \n')


def show_all(file_name):
    with open(file_name, 'r', encoding='utf8') as data:
        print(data.read())
    print()
    pause()


def read_file_into_strings(file_name):
    result = []
    with open(file_name, 'r', encoding='utf8') as data:
        for line in data:
            result.append(line.strip('\n'))
    return result


def find_user():
    name = input('Введите любую часть имени, отчества или фамилии: ')
    print()
    user_list = read_file_into_strings(fileName)
    for user in user_list:
        if name in user:
            print(user)
    print()
    pause()


def find_number():
    number = input('Введите номер телефона в формате +79001234567: ')
    print()
    user_list = read_file_into_strings(fileName)
    for user in user_list:
        if number in user:
            print(user)
    print()
    pause()
    return user


def add_new_contact(file_name):
    with open(file_name, 'a', encoding='utf8') as data:
        data.writelines(input('Введите через запятую Фамилию, Имя, Отчество, Номер телефона: ') + '\n')


def correct_number():
    user = find_number().split()
    user[3] = input('Введите новый номер телефона в формате +79001234567: ')
    pause()


def read_file_into_words(file_name):
    result = []
    with open(file_name, 'r', encoding='utf8') as data:
        for line in data:
            result.append(line.split(''))
    return result

# add_new_contact(fileName)
# print(type(read_file(fileName)))
# print(read_file(fileName))
# find_user(read_file(fileName))

while True:
    print('''Меню:
     1 - Показать все записи
     2 - Найти запись по вхождению частей имени
     3 - Найти запись по телефону
     4 - Добавить новый контакт
     5 - Удалить контакт
     6 - Изменить номер телефона у контакта
     7 - Выход\n''')
    
    action = int(input('Введите номер действия: '))
    print()

    match action:
        case 1:
            show_all(fileName)
        case 2:
            find_user()
        case 3:
            find_number()
        case 4:
            add_new_contact(fileName)
        case 5:
            pass
        case 6:
            correct_number()
        case 7:
            break