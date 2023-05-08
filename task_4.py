import sys
from utils import print_intro

print_intro()


def get_input():
    while True:
        input_data = input("Enter an integer m or 'exit' to quit: ")
        if input_data.lower() == 'exit':
            sys.exit()
        try:
            m = int(input_data)
            return m
        except ValueError:
            print("Error: Please enter an integer or 'exit' to quit.")


def find_fibonacci(m):
    if m <= 1:
        return 1
    f1, f2 = 1, 1
    while True:
        fn = f1 + f2
        if fn > m:
            return fn
        f1, f2 = f2, fn


if __name__ == '__main__':
    while True:
        m = get_input()
        result = find_fibonacci(m)
        print(f"The first Fibonacci number greater than {m} is {result}.")