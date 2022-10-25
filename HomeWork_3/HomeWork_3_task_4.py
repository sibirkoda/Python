"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

str1 = ""
number_dec = int(input('Введите натуральное число: '))
number = number_dec

while (number > 1):
    str1 = str(number % 2) + str1
    number = int (number / 2)
str1 = str(number) + str1
print('Число', number_dec, 'в двоичной системе выглядит так:', str1)