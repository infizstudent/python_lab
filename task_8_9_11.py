def decimal_to_binary(decimal):
    return bin(decimal)[2:]


def binary_to_decimal(binary):
    return int(binary, 2)


def validate_binary_input(binary):
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        print('Error: Invalid binary number entered')


def process_choice(choice):
    if choice == '1':
        decimal_number = int(input('Enter a decimal number: '))
        binary_number = decimal_to_binary(decimal_number)
        print(f'{decimal_number} in Decimal is {binary_number} in Binary.')

    elif choice == '2':
        binary_number = input('Enter a binary number: ')
        if validate_binary_input(binary_number):  # need to remove duplicate validate
            decimal_number = binary_to_decimal(binary_number)
            print(f'{binary_number} in Binary is {decimal_number} in Decimal.')
        else:
            print('Invalid binary number.')

    else:
        print('Invalid choice.')


if __name__ == '__main__':
    choice = input('Select an option (1 - Decimal to Binary, 2 - Binary to Decimal): ')
    process_choice(choice)
