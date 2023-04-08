# TODO здесь писать код
import math


def detector(x, y, r):
    z = math.sqrt(x ** 2 + y ** 2)
    if z <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

print('Введите координаты монетки:')
x = float(input('x: '))
y = float(input('y: '))
r = int(input('Введите радиус: '))
detector(x, y, r)
