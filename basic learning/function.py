# function definition


def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


x = float(input('x='))
n = float(input('n='))
print(power(x, n))

# 二元一次方程


import math


def equation(a, b, c):
    list1 = [a,b,c]
    for x in list1:
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')

    p = b*b-4*a*c
    if p >= 0:
        x1 = (-b + math.sqrt(p))/(2*a)
        x2 = (-b - math.sqrt(p))/(2*a)
    else:
        x1 = None
        x2 = None
    return {x1, x2}


a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
print(equation(a, b, c))
