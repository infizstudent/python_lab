from utils import validate_input


def count_digits(n):
    if n == 0:
        return 1

    n = abs(n)
    count = 0
    while n:
        count += 1
        n //= 10
    return count


if __name__ == '__main__':
    n = validate_input()
    digit_count = count_digits(n)
    print(f'Number of digits in the number: {digit_count}')
