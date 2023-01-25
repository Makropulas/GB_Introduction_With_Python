# Вычислить значение выражения

# Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a // b
    elif op == '*':
        return a * b


def first_operations(str): 
    m = str.split()
    new_list = []
    for i in range(len(m)):
        if m[i] == '*' or m[i] == '/':
            result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
            m[i-1] = result
            m[i] = m[i+1] = ''

    for i in range(len(m)):
        if m[i] != '':
            new_list.append(m[i])

    return new_list


def second_operations(m):
    result = int(m[0])
    for i in range(1, len(m) - 1, 2):
        result = calc(result, int(m[i + 1]), m[i])
    return result


n = '12 - 4 * 2 + 6 / 3'

print(n, '=', second_operations(first_operations(n)))
