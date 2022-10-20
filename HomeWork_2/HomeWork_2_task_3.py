"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }
"""
n = int(input('Введите натуральное число: '))
def function(x):
    return round((1 + 1 / x)**x, 2)
arr = {}
sum = 0
for i in range(1, n+1):
    arr[i] = function(i)
    sum += function(i)
print('Для n =', n, ': ',  arr)
print('Их сумма равна: ', round(sum, 2))