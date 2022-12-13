# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

while True:
    number = input('Введите трёхзначное число: ')
    sum = 0
    if (number.isdigit() == False) or (len(number) != 3):
        print('Трёхзначное число - это три цифры')
    else:
        for digit in number:
            sum += int(digit)
        print(f'Cумма цифр в числе {number} -> {sum}')
        break
