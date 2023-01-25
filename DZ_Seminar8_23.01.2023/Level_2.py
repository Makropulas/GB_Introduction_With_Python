# Вычислить значение выражения

# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4

n = '22 + 300 - 14 + 10 + 10'
m = n.split()
print(m)


def calc (a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '*':
        return a * b


a = int(m[0])
b = int(m[2])
c = m[1]

result = calc(a, b, c)

for i in range(3, len(m) - 1, 2):
    result = calc(result, int(m[i + 1]), m[i])
    print(m[i], m[i + 1])
    print(result)
