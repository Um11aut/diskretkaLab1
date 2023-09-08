def calculRectArea(x1:int, y1:int, x2: int, y2:int):
    if x1 == x2 or y1 == y2:
        return 0
    a = abs(x1) + abs(x2)
    b = abs(y1) + abs(y2)
    return a*b

def calculRectSum(x1:int, y1:int, x2: int, y2:int):
    if x1 == x2 or y1 == y2:
        return 0
    a = abs(x1) + abs(x2)
    b = abs(y1) + abs(y2)
    return 2 * (a+b)

