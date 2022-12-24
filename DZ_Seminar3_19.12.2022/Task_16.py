# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2


import random

n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите число, которое необходимо найти: '))
if x < 1 or x > n/2:
    print('Такого числа нет в массиве')
    quit()
array = []

for item in range(0, n):
    array.append(round(random.randint(1, int(n/2))))
print(array)

count = 0
for i in array:
    if i == x:
        count += 1
print(f'Запрошенное число встречается {count} раз(а)')