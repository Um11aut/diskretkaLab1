def solveTask10(arr: []):
    average = sum(arr) / len(arr)

    result_array = []

    for element in arr:
        if element > average:
            result_array.append(element - 18)
        else:
            result_array.append(element)
    return result_array