def validate_decimal_input(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Invalid input. Expected a non-negative integer.")


def validate_binary_input(binary):
    if not isinstance(binary, str) or not set(binary).issubset({'0', '1'}):
        raise ValueError("Invalid input. Expected a binary string.")


def decimal_to_binary(decimal):
    validate_decimal_input(decimal)
    return '0' if decimal == 0 else decimal_to_binary(decimal // 2) + str(decimal % 2)


def binary_to_decimal(binary):
    validate_binary_input(binary)
    return sum(int(binary[i]) * (2 ** (len(binary) - i - 1))
               for i in range(len(binary)))


if __name__ == '__main__':
    try:
        decimal_number = int(input('Enter a decimal number: '))
        validate_decimal_input(decimal_number)
        binary_number = decimal_to_binary(decimal_number)
        print(f'{decimal_number} in Decimal is {binary_number} in Binary.')
    except ValueError as e:
        print(f"Error: {str(e)}")

    try:
        binary_number = input('Enter a binary number: ')
        validate_binary_input(binary_number)
        decimal_number = binary_to_decimal(binary_number)
        print(f'{binary_number} in Binary is {decimal_number} in Decimal.')
    except ValueError as e:
        print(f"Error: {str(e)}")
