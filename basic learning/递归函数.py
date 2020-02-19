def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(4))


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)


print(fact(5))


def minmax(L):
    if len(L) == 0:
        return None, None
    else:
        min = L[0]
        max = L[0]
    for n in L:
        if n < min:
            min = n
        if n > max:
            max = n
    return min, max


r = []
a = 1
while a <= 100:
    r.append(a)
    a = a+5
print(r)

print(minmax(r))

for ch in 'ABCasdf':
    print(ch)

from collections import Iterable
a = input('enter the iterable words:')
if isinstance(a, Iterable):
    print('True')
else:
    print('False')

for ch in a:
    print(ch)

