# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

fileName = 'Phonebook.txt'

def pause():
    input('Для продолжения нажмите Enter ')


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
    name = input('Введите Фамилию, Имя или Отчество (с большой буквы): ')
    print()
    string_return = ''
    user_list = read_file_into_strings(fileName)
    for user in user_list:
        if name in user:
            print(user)
            string_return = user
    print()
    pause()
    return string_return


def find_number():
    number = input('Введите номер телефона в формате +79001234567: ')
    print()
    user_list = read_file_into_strings(fileName)
    for user in user_list:
        if number in user:
            print(user)
    print()
    pause()
    return number


def add_new_contact(file_name):
    with open(file_name, 'a', encoding='utf8') as data:
        data.write('\n')
        data.writelines(input('Введите через пробел Фамилию, Имя, Отчество, Номер телефона: '))


def correct_number(file_name):
    old_number = find_number()
    new_number = input('Введите новый номер телефона в формате +79001234567: ')
    with open(file_name, 'r', encoding='utf8') as data:
        new_data = data.read().replace(old_number, new_number)
    with open(file_name, 'w', encoding='utf8') as data:
        data.write(new_data)
    print()
    pause()


def delete_user(file_name):
    user = find_user()
    with open(file_name, 'r', encoding='utf8') as data:
        new_data = data.read().replace(user, '').strip('\n')
    with open(file_name, 'w', encoding='utf8') as data:
        data.write(new_data)
    print()
    pause()


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
            delete_user(fileName)
        case 6:
            correct_number(fileName)
        case 7:
            break