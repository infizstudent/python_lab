def validate_input(input_str):  # no handling of negative numbers
    while True:
        try:
            value = int(input_str)
            if value >= 0:
                return value
            else:
                print('Invalid input. Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def is_leap_year(number_year):
    return number_year % 4 == 0 and (number_year % 100 != 0 or number_year % 400 == 0)


if __name__ == '__main__':
    year_input = input('Enter the year: ')

    if not validate_input(year_input):
        print('Invalid input. Please enter a valid year.')
    else:
        year = int(year_input)
        if is_leap_year(year):
            print('Leap year')
        else:
            print('Ordinary year')
