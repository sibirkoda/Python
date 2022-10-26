s1 = [['+19', '0'], ['-82', '1'], ['+51', '2'], ['-94', '3'], ['2', '4'], ['-82', '5']]
s2 = [['0', '0'], ['-2', '1'], ['-41', '2'], ['+31', '3']]

# функция сложения полиномов
max0 = max(len(s1), len(s2))
min0 = min(len(s1), len(s2))

i=0
list_basa = []
while i < max0:
    list_basa.append([int(0),str(i)])
    i+=1

for i in range (min0):
    list_basa[i][0]= int(s1[i][0])+int(s2[i][0])

if len(s1) > len(s2):
    for i in range (min0, max0):
        list_basa[i][0]= int(s1[i][0])
elif len(s1) < len(s2):
    list_basa[i][0]= int(s2[i][0])


print(list_basa)
# print(s1[][])
# print()
