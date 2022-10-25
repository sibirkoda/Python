"""
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

import random
n = int(input('Введите число элементов в списке: '))
list1 = []
for i in range(n):
    r = random.randint(1, 10)
    list1.append(r)
print('Исходный список элементов: ', list1)

list2=[]
while list1 != []:
    p = list1[0]
    list2.append(p)
    list1 = list(filter(lambda x:  x != p, list1))
print('Список неповторяющихся элементов исходной позиции: ', list2)