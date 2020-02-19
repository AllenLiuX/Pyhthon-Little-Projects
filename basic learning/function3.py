

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum


numbers = eval(input())  # 输入list
sum = calc(*numbers)
print('sum=', end='')  # 不换行
print(sum)


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 12, city = 'Beijing')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


a = input('Name:')
b = input('age:')
person(a, b, city='Beijing')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Bejing', 'sexuality': 'Male'}
a = input('Name:')
b = input('age:')
person(a, b, **extra)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
