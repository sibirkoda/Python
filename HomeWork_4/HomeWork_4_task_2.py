"""
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input('Введите натуральное число: '))
list1 = [x for x in range(2, n+1)]
list2 = []
while list1 != []:
    p = list1[0]
    list2.append(p)
    list1 = list(filter(lambda x: x % p != 0, list1))
list3 = list(filter(lambda x: n % x == 0, list2))
list3.insert(0,1)
print('Список простых множителей введенного числа', n, ':', list3)
