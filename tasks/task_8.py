def solveTask8(a: int, b: int):
    if b < a:
        print("B має бути більше А")
    else:
        count = 0
        print("Числа:")

        for number in range(a, b + 1):
            print(number)
            count += 1

        print("К-сть чисел у діапазоні", count)
