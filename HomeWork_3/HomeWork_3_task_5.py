"""
Задайте число.
Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

n = int(input('Введите целое число: '))
list1 = []

def fib_plus(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib_plus(n-1) + fib_plus(n-2)

def fib_minus (n):
    if (n == -1):
        return 1
    elif (n == -2):
        return -1
    else:
        return fib_minus(n+2) - fib_minus(n+1)

for i in range(n, 0, -1):
    list1.append(fib_minus(-i))

for i in range(0, n+1):
    list1.append(fib_plus(i))

print(list1)
