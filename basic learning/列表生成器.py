print([x*x for x in range (1,100) if x % 2 == 0])
print([m+n for m in range (1,5) for n in range (1,3)])
print([m+n for m in range (1,5) for n in range (1,10) if n % 2 == 1])
A = [a*b for a in range (1,100) for b in range (1,2)]
A.insert(2, '\n')
print(A)

g = (x * x for x in range (10))
for n in g:
    print(n)


def feb(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b, = b, a+b
        n = n+1
    return 'done'


for n in feb(500):
    print(n)