def validate_input():
    while True:
        try:
            return float(input('Enter a number: '))
        except ValueError:
            print('Invalid input')
