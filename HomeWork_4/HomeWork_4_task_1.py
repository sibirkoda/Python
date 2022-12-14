"""
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

3,1415926535897932384626433832795
"""

pi = 3.1415926535897932384626433832795 
# задали число ПИ, чтобы затем сравнить насколько точно мы вычислили

print('Введите точность вычисления числа ПИ, например, в таком виде: 0.001')
d = float(input('Диапазон допустимых значений точности: 10^{-1} ≤ d ≤10^{-10}: '))

# Будем использовать ряд Нилоканта π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
# Определим функцию равную элементу ряда
def f(n):
    return 4/(n*(n+1)*(n+2))

sum1 = 0
sum2 = 3
znak = 1
count = 2

while (abs(sum2 - sum1) > d):
    sum1 = sum2
    sum2 = sum2 + f(count) * znak
    count += 2
    znak *= (-1)

print (sum2)
print('Точность вычисления равна:',  abs(pi - sum2), 'что меньше требуемой точности', d)
