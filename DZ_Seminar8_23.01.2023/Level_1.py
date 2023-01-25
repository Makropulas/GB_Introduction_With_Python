# Вычислить значение выражения

# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

n = '2 + 3'

m = n.split()

a = int(m[0])
b = int(m[2])
c = m[1]

if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '/':
    print(a/b)
elif c == '*':
    print(a*b)

