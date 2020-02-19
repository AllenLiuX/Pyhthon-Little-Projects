list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

from functools import reduce
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


from functools import reduce
def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


P = reduce(fn, map(char2num, '13579'))
print(P)


def normalize(name):
    if len(name) > 1:
        return name[:1].upper() + name[1:].lower()
    if len(name) == 1:
        return name.upper()


name = input('name is:')
print(normalize(name))


def prod(s):
    def pro(a, b):
        return a*b
    return reduce(pro, s)


s = [3, 5, 7, 9]
print(prod(s))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1,2,3)
print(f())

L = list(filter(lambda n: n%2==1, range(1, 20)))
print(L)