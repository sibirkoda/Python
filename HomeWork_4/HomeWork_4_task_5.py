"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""
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

"""
s1 = '94*x^3-51*x^2+82*x^1+19=0'
temp_s1 = s1.replace('=0', '')

# Функция формирует список из индексов символов "+" и "-" в строке
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

# Функция для разбития многочлена на слагаемые и формирование из них списка
def Terms(s):
    j = 0
    terms = []
    for i in index1:
        terms.append(temp_s1[j:i])
        j = i
    terms.append(temp_s1[index1[-1]:])
    for item in terms:
        i=0
        if item[0] != '+':
            if item[0] != '-':
                terms[i] = '+' + item
        i+=1
    for item in terms:
        i=0
        if item.find('*x^') == -1:
            terms[i] = item +'*x^0'
        i+=1
    
    return terms

print (s1)
index1 = IndexZnak(temp_s1)
terms1 = Terms(index1)

print(index1)
print(terms1)



cor1 = []
for item in terms1:
    cor1.append(item.split('*x^'))

print(cor1)
