def print_intro():
    print('Introduction to programming: Task 4')
    print('Kravchuk Artem')


def validate_input():
    while True:
        try:
            return float(input('Enter a number: '))
        except ValueError:
            print('Invalid input')
