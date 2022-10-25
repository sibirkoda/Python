"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

list1 = []
count = 0
while True:
    st = input('Введите следующий элемент списка (целое число): ')
    if st == "":
        break
    list1.append(int(st))
    count += 1
print('Вы ввели список: ', list1)

if (count % 2 == 0):
    i = int(count / 2)
else:
    i = int(count / 2 + 1)

list2 = []

for j in range(i):
    list2.append(list1[j]*list1[-(j+1)])

print(list2)
