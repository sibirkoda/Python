"""
Задача 4.
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

"""
a = int(input ('Введите первое число: '))
if (a % 5 == 0 and a % 10 == 0 and a % 30 != 0):
    print('да,' , a, 'кратно 5 и 10')
elif (a % 15 == 0 and a % 30 != 0):
        print('да,' , a, 'кратно 15')
else:
    print('нет, не кратно 5 и 10 или 15')