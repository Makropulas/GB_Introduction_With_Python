import function as fn


menuitems = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Вывод водителей"),
        ("4", "Добавление водителей"),
        ("5", "Вывод маршрута"),
        ("6", "Добавление маршрута"),
        ("7", "Детализация маршрута"),
        ("8", "Выход")]


while True:
    print()
    for i in menuitems:
        print(i[0],i[1])
    print()

    text = input("Введите номер: ")
    print()
    if text == '1':
        print(f'Автобусы: {fn.print_bus()}')
        print()
        fn.pause()
    elif text == '2':
        fn.add_bus()
        print()
        fn.pause()
    elif text == '3':
        print(f'Водители: {fn.print_driver()}')
        print()
        fn.pause()
    elif text == '4':
        fn.add_driver()
        print()
        fn.pause()
    elif text == '5':
        print(f'Маршруты: {fn.print_route()}')
        print()
        fn.pause()
    elif text == '6':
        fn.add_route()
        print()
        fn.pause()
    elif text == '7':
        fn.print_detail_route()
        print()
        fn.pause()
    elif text == '8':
        break
    else:
        print('Неверная команда. Возврат в меню')
        print()
        fn.pause()
