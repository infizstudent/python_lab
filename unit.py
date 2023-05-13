def get_input() -> (float, float):
    while True:
        try:
            a = float(input('Enter a positive number a: '))
            x = float(input('Enter any leading positive number x: '))
            if a <= 0 or x <= 0:
                raise ValueError
            return a, x
        except ValueError:
            print("Invalid input, please enter a positive number.")