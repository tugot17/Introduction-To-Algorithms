'''
Chapter2 ex 4. Add 2 binarty numbers (number is represented as an array)
'''

def add_binnary_numbers(x, y):
    x.reverse()
    y.reverse()

    while (len(y) < len(x)):
        y.append(0)

    while (len(x) < len(y)):
        x.append(0)

    buffer = 0
    result = []

    for i in range(len(x)):
        sum = x[i] + y[i] + buffer

        if sum == 0:
            result.append(0)

        if sum == 1:
            result.append(1)

        if sum == 2:
            result.append(0)
            buffer = 1

        if sum == 3:
            result.append(1)

    if buffer != 0:
        result.append(1)

    result.reverse()
    return result




