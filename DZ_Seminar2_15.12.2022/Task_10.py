# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

coins = int(input('Введите количество монет: '))
side_coins = []

for item in range(0, coins):
    side_coins.append(round(random.randint(0, 1)))

print(side_coins)

heads = tails = 0
for item in side_coins:
    if item == 0:
        heads += 1
    else:
        tails += 1
if heads < tails:
    min = heads
else:
    min = tails

print(f'Количество монет, которые нужно перевернуть: {min}')
