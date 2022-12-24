# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число, которое необходимо проверить: '))
if x < 1 or x > n:
    print(f'По условиям задачи, такое число запрашивать нельзя. Введите число от 1 до {n}')
    quit()

array = []
for item in range(0, n):
    array.append(random.randint(1, n))
print(array)

w = x - 1
y = x + 1
res = 0

while res == 0:
    for i in array:
        if i == x:
            res = i
            break
        else:
            if i == w:
                res = i
            if i == y and res == 0:
                res = i   # Если найден 'y', то до конца массива продолжается поиск 'w' или 'x'
    w -= 1
    y += 1
print(f'Ответ: {res}')
