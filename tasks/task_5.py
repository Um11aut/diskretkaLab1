def calc5a(a: int, b: int, c: int):
    if a % 1 == 0 and b%1 == 0 and c%1 == 0:
        if a < b and b < c:
            return True
    
    return False

def calc5b(a: int, b: int, c: int):
    if a % 1 == 0 and b%1 == 0 and c%1 == 0:
        if a > 0 or b > 0 or c > 0:
            return True
    
    return False

def calc5c(a: int, b: int, c: int):
    if a % 1 == 0 and b%1 == 0 and c%1 == 0:
        positive_count = 0
        if a > 0:
            positive_count += 1
        if b > 0:
            positive_count += 1
        if c > 0:
            positive_count += 1

        if positive_count == 1:
            return True
            
    return False
