# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
pow = 0
result = ''
while True:
    num = 2 ** pow
    if num <= n:
        result += f'{str(num)} '
        pow += 1
    else:
        break
print(result)