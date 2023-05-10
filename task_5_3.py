from typing import Tuple


def get_input() -> Tuple[float, float]:
    while True:
        try:
            a = float(input('Enter a positive number a: '))
            x = float(input('Enter any leading positive number x: '))
            if a <= 0 or x <= 0:
                raise ValueError
            return a, x
        except ValueError:
            print("Invalid input, please enter a positive number.")


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
