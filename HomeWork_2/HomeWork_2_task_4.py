"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random
n = int(input('Введите натуральное число: '))
s = []
for i in range(n):
    r = random.randint(-n, n)
    s.append(r)
print('Будем искать произведение элементов в этом списке: ', s)

print('Далее вводите номера позиций, которые необходимо перемножить.')
print('Допустимые значения: от 0 до ', n-1, '.')
print('Окончанием ввода будет - нажатие ENTER без ввода числа.')

data = open('file.txt', 'w')
while True:
    st = input('Укажите позицию для вычисления: ')
    if st == "":
        break
    data.write(st+"\n")
data.close()

result = 1
data = open('file.txt', 'r')
for line in data:
    if line == "":
        break
    result *= s[int(line)]
data.close()
print()

print('Произведение элементов на указанных позициях равно: ', result)

