def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

s = '     sfdf '
print(trim(s))

r = []
a = 1
while a <= 100:
    r.append(a)
    a = a+1
print(r)

L = []
for a in range (0,100):
    L.append(a)
print(L)