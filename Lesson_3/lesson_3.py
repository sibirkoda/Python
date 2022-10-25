# def f(x):
#     return x**2
# g = f
# print(type(g))
# print(f(2))

# def calc1(x):
#     return x+10
# print (calc1(10))
# def calc2(x):
#     return x*10
# print (calc2(10))
# def math (op, x):
#     print (op(x))
# math(calc2, 10)

# def sum(x, y):
#     return x+y
# sum = lambda x,y : x+y
# def mylt(x, y):
#     return x*y
# def math(op, x, y):
#     print(op(x, y))
#     # return print (op(x,y))
# math(f, 1, 2)

# list = []
# # for item in range(2,20,2):
# #     list.append(item)
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(0, 21) if i % 2 == 0]
# print(list)

"""
f = open('file3.txt', 'r')
data = f.read() + ' '
f.close()
numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out)
"""

"""
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
print(data)
res = select(int, data)
print(res)
res = where(lambda x: not x % 2, res)
res = select (lambda x: (x, x**2), res)
print(res)
"""
"""
li = [x for x in range(1, 20)]
print(li)
li = list(map (lambda x : x+10, li))
print(li)
"""
"""
data = list(map(int,input().split()))
print (data)
"""

data = [x for x in range(1, 10)]
res = list(filter(lambda x: x % 2 == 0, data))
print(data)
print(res)
