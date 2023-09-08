def solveTask11(N: int):
    if N <= 1:
        print("Число має бути більше 1")
    else:
        is_prime = True  # Предполагаем, что число простое

        for i in range(2, N):
            if N % i == 0:
                is_prime = False  # Если есть делитель, то число не простое
                break

        if is_prime:
            print("число {} просте".format(N))
        else:
            print("число {} не просте".format(N))

