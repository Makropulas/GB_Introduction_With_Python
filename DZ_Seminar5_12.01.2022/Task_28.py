# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        return a + sum(a - (a - 1), (b - 1))


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'{a} + {b} = {sum(a, b)}')


# --------------------------------------------------------------------------------------------------------------------
# Проверка работы рекурсии в попытках понять рекурсию (я так и не могу её в голове прокрутить на этапе написания) :'-(
# --------------------------------------------------------------------------------------------------------------------

# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(3000)
# print(sys.getrecursionlimit())

# def sum(a, b):
#     if b == 0:
#         print(f'a = {a} | b = {b}')
#         return a
#     else:
#         print(f'a = {a} | b = {b}')
#         return a + sum(a - (a - 1), (b - 1))


# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))

# print(f'{a} + {b} = {sum(a, b)}')

# # Максимально получилось с помощью этой рекурсии сложить 2128+2128. Дальше не досчитывает и вылетает

# --------------------------------------------------------------------------------------------------------------------

# А это решение я позже нагуглил (было написано на плюсах, перевёл в питон). Красиво. 
# Я вроде понял его, но такое чувство что не до конца, т.к. сомневаюсь, что сам под другую задачу допру своей головой ((
# Решил по-честному сдать именно своё решение, а это оставить себе на память. Может когда-то осознаю


# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a + 1, b - 1)   # <---- Нагуглил эту строку


# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))

# print(f'{a} + {b} = {sum(a, b)}')