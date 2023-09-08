import math


def func(x: float, y: float, z: float):
    up = x + z*z + y/4
    down = z*(y-2) + math.pow(z*z + 4, -1)
    return up/down

