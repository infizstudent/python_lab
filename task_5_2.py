def is_valid_input(n):
    if n % 1 != 0:
        return False
    return True


def count_digits(n):
    n = abs(n)
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


if __name__ == '__main__':
    try:
        n = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        if not is_valid_input(n):
            print("Invalid input")
        else:
            digit_count = count_digits(n)
            print(f"Number of digits in the number: {digit_count}")
