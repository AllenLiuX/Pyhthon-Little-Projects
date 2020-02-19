s = input('I have:')
A = int(s)
if A > 100:
    print(A+2)
else:
    print('sorry')

sum = 0
for a in list(range(5)):
    sum = sum+a
print(sum)

sum = 10
n = 200
while n > 0:
    sum = sum+n
    n = n-2
print(sum)

n = 1
while n <= 100:
    if n > 4:
        break
    print(n)
    n = n+1
print('End')

n = 1
while n <= 20:
    n = n+1
    if n == 6:
        continue
    print(n)
print('End')
