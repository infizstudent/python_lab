import math

precision = 4


def series_sum(x, precision):
    sum = 0
    term = 1
    n = 0
    while abs(term) >= 10 ** (-1 * precision):
        term = 2 ** n * math.factorial(n) / n ** n
        sum += term
        n += 1
    return sum


if __name__ == "__main__":
    result = series_sum(1, precision)
    print(round(result, precision))