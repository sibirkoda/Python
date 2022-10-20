"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
n = int(input('Введите натуральное число: '))
massiv1 = [1]
number = 1
count = 2
while (count < n+1):
    number *= count
    massiv1.append(number)
    count += 1
print(massiv1)
