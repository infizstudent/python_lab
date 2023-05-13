from unit import get_input


def calculate_square_root(a: float, x: float, epsilon: float = 0.0001) -> float:
    xn = x
    xn1 = 0.5 * (xn + a / xn)
    while abs(xn1 - xn) > epsilon:
        xn, xn1 = xn1, 0.5 * (xn1 + a / xn1)
    return round(xn1, 4)


if __name__ == '__main__':
    a, x = get_input()
    square_root = calculate_square_root(a, x)
    print(f'The square root of {a} is {square_root}')