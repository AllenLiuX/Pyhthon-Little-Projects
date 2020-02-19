import math
def move(x, y, step, angle):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx, ny

x = float(input('x ='))
y = float(input('y ='))
step = float(input('step ='))
angle = float(input('angle ='))
x, y = move(x, y, step, angle)
print(x, y)