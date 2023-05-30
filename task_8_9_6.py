def validate_input(input_str):
    while True:
        try:
            value = int(input_str)
            if value >= 0:
                return value
            print('Invalid input. Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
        input_str = input('Enter the year: ')


def is_leap_year(number_year):
    return number_year % 4 == 0 and (number_year % 100 != 0 or number_year % 400 == 0)


if __name__ == '__main__':
    year = validate_input(input('Enter the year: '))
    if year:
        print('Leap year' if is_leap_year(year) else 'Ordinary year')
    else:
        print('Invalid input. Please enter a valid year.')
