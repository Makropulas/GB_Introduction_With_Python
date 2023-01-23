def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').replace(' ', '').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def find_keyword(name, keyword):
    our_lists = read_data_from_file(name)
    for our_list in our_lists:
        if keyword in our_list:
            return our_list

def pause():
    input('Для продолжения нажмите Enter ')


def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))
    
def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))

def print_detail_route():
    route = input('Введите номер маршрута: ')
    print()
    route_list = find_keyword('route.txt', route)
    print('Данные маршрута: ', route_list)
    bus_list = find_keyword('bus.txt', route_list[2])
    print('Данные автобуса: ', bus_list)
    driver_list = find_keyword('driver.txt', route_list[3])
    print('Данные водителя: ', driver_list)
