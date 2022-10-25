"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""

import random
# функция-генератор знака у элемента многочлена


def znak():
    if random.randint(0, 2) == 0:
        a = 1
    else:
        a = -1
    return a

# функция создает многочлен


def create(k):
    s1 = []
    for i in range(0, k+1):
        s1.append(znak()*random.randint(1, 100))
    s2 = str(s1[0]) + '*x^'+str(k)
    for i in range(1, k):
        if (s1[i] > 0):
            s2 += '+'+str(s1[i]) + '*x^'+str(k-i)
        else:
            s2 += str(s1[i]) + '*x^'+str(k-i)
    if (s1[k] > 0):
        s2 += '+'+str(s1[k])+'=0'
    else:
        s2 += str(s1[k])+'=0'
    return s2


# создаем файлы и вписываем туда многочлены
k = int(input('Введите степень многочлена k1, с которыми будем работать: '))
s = create(k)
file = open('file5.txt', 'w')
file.write(s)
file.close()
s = create(k)
file = open('file6.txt', 'w')
file.write(s)
file.close()

# Таким образом, мы сгенерировали многочлены и вписали их в файлы.
# Далее будем считывать их, складывать и впишем в новый файл их сумму
with open('file5.txt', 'r') as file:
    s1 = file.readline()
with open('file6.txt', 'r') as file:
    s2 = file.readline()
print(s1)
print(s2)
