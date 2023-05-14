import math

PRECISION = 4


def calculate_series_sum(x, precision):
    sum = 0
    term = 1
    n = 0
    while abs(term) >= 10 ** (-1 * precision):
        term = (x ** n / n ** n) * math.factorial(n) / math.exp(n)
        sum += term
        n += 1
    return round(sum, precision)


if __name__ == '__main__':
    result = calculate_series_sum(1, PRECISION)
    print(result)
