# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    if b == 1:
        return a
    else:
        return a * exponentiation(a, b - 1)

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'{a} в степени {b} = {exponentiation(a, b)}')