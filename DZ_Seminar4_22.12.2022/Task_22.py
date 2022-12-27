# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12


import random

def fill_array(num, x):
    for i in range(x):
        num.append(random.randint(1, 20))

n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов второго набора чисел: '))
print()

array_of_numbers_one = []
fill_array(array_of_numbers_one, n)
print('Первый набор чисел', array_of_numbers_one)
set_of_numbers_one = set(array_of_numbers_one)

array_of_numbers_two = []
fill_array(array_of_numbers_two, m)
print('Второй набор чисел', array_of_numbers_two)
set_of_numbers_two = set(array_of_numbers_two)

result = []
for i in set_of_numbers_one:
    for j in set_of_numbers_two:
        if i == j:
            result.append(i)
result.sort()
print('Встречаются в обоих наборах', result)
