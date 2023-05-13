import sys
from utils import print_intro

print_intro()

def get_input():
    while True:
        input_data = input("Enter an integer input_number or 'exit' to quit: ")
        if input_data.lower() == 'exit':
            sys.exit()
        try:
            input_number = int(input_data)
            return input_number
        except ValueError:
            print("Error: Please enter an integer or 'exit' to quit.")

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
    while True:
        input_number = get_input()
        result = find_fibonacci(input_number)
        print(f'The first Fibonacci number greater than {input_number} is {result}.')
