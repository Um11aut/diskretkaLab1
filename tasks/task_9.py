def get_reverse(N: int):
    if N <= 0:
        print("Число має бути більше нуля.")
    else:
        reversed_number = 0
        original_number = N

        while N > 0:
            # Получаем последнюю цифру числа N
            last_digit = N % 10

            # Добавляем её к обратному числу
            reversed_number = reversed_number * 10 + last_digit

            # Убираем последнюю цифру из числа N
            N = N // 10

        print("Початкове: ", original_number, "справа наліво: ", reversed_number)

