
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def addTwoNumbers(l1, l2):
    a = l1[0] + l2[0]
    b = l1[1] + l2[1]
    c = l1[2] + l2[2]

    if l1[1] + l2[1] >= 10:
        c += 1
        b = b - 10
    if l1[2] + l2[2] >= 10:
        b += 1
        a = a - 10

    return [a,b,c]


print(addTwoNumbers(l1, l2))



def addTwoNumbers(l1,l2):
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    c = 0
    d = 0
    for n in l1:
        c = c * 10 + n

    for m in l2:
        d = d * 10 + m

    print(c, d)


#print(addTwoNumbers(l1, l2))

