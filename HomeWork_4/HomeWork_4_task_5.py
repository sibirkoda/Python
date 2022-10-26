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
# Далее уже приступим непосредственно к выполнению задачи:
# считаем многочлены из двух файлов, сложим их и впишем сумму в новый файл

with open('file5.txt', 'r') as file:
    s1 = file.readline()
with open('file6.txt', 'r') as file:
    s2 = file.readline()

# Функция формирует список из индексов символов "+" и "-" в строке, далее это пригодится
def IndexZnak(s):
    last = len(s)
    terms = []
    first = 1
    while (first < last):
        l = s.find('-', first, last)
        if l == -1:
            break
        terms.append(l)
        first = l+1
    first = 0
    while (first < last):
        l = s.find('+', first, last)
        if l == -1:
            break
        terms.append(l)
        first = l+1
    return terms

# Функция для разбития многочлена из файла на слагаемые и формирование из них списка
def Terms(s0):
    s1 = sorted(IndexZnak(s0))
    s2 = s0.replace('=0', '')
    j = 0
    terms = []
    for i in s1:
        terms.append(s0[j:i])
        j = i
    terms.append(s2[s1[-1]:])
    for item in terms:
        i = 0
        if item[0] != '+':
            if item[0] != '-':
                terms[i] = '+' + item
        i += 1
    i = 0
    for item in terms:
        if item.find('*x^') == -1:
            terms[i] = item + '*x^0'
        i += 1
    return terms

# Функция создания списка списков: коэффициент и степень, заполнение недостающих слагаемых
def Poly(s):
    cor = []
    for item in s:
        cor.append(item.split('*x^'))
    cor = sorted(cor, key=lambda x: x[1])
    max0 = int(max(cor, key=lambda x: x[1])[1])
    i = 0
    list_basa = []
    while i < max0+1:
        list_basa.append([str(0), str(i)])
        i += 1
    for item in cor:
        j = int(item[1])
        list_basa[j] = item
    return list_basa

# функция сложения двух списков полиномов
def Sum(s_1, s_2):
    max0 = max(len(s_1), len(s_2))
    min0 = min(len(s_1), len(s_2))
    i = 0
    list_basa = []
    while i < max0:
        list_basa.append([int(0), str(i)])
        i += 1

    for i in range(min0):
        list_basa[i][0] = int(s_1[i][0])+int(s_2[i][0])

    if len(s_1) > len(s_2):
        for i in range(min0, max0):
            list_basa[i][0] = int(s_1[i][0])
    elif len(s_1) < len(s_2):
        list_basa[i][0] = int(s_2[i][0])

    return list_basa

# функция преобразования списка в строку - уравнение
def NewF(s0):
    str0 = ''
    i = False
    for item in s0:
        if item[0] > 0 and not i:
            str0 = str0 + str(item[0]) + '*x^'+str(item[1])
            i = True
        elif item[0] > 0 and i:
            str0 = str0 + '+'+str(item[0]) + '*x^'+str(item[1])
        elif item[0] < 0:
            str0 = str0 + str(item[0]) + '*x^'+str(item[1])
    str0 = str0 + '=0'
    str1 = str0.replace('*x^0','')
    return str1

terms1 = Terms(s1)
terms2 = Terms(s2)
cor1 = Poly(terms1)
cor2 = Poly(terms2)
der = Sum(cor1, cor2)
der1 = NewF(der)
print(der1)

file = open('file7.txt', 'w')
file.write(der1)
file.close()