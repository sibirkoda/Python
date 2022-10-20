"""
Реализуйте алгоритм перемешивания списка.
"""
import random

print('Далее вводите элементы списка.')
print('Окончанием ввода будет - нажатие ENTER без ввода символов.')

s = []
count = 0
while True:
    st = input('Введите следующий элемент списка: ')
    if st == "":
        break
    s.append(st)
    count += 1
print(s)

snew = []
while count > 1:
    r = random.randint(1, count-1)
    snew.append(s[r])
    s.pop(r)
    count -= 1
snew.append(s[0])
print(snew)
