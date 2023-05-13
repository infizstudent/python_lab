from utils import print_intro, validate_input

print_intro()


def find_fibonacci(input_number):
    if input_number <= 1:
        return 1
    f1, f2 = 1, 1
    while True:
        fn = f1 + f2
        if fn > input_number:
            return fn
        f1, f2 = f2, fn


if __name__ == '__main__':
    input_number = validate_input()
    result = find_fibonacci(input_number)
    print(f'The first Fibonacci number greater than {input_number} is {result}.')
