from utils import validate_input


def validate_operations(first_number, second_number, operation_func):
    try:
        return operation_func(first_number, second_number)
    except ZeroDivisionError:
        print('Error: Division by zero!')
        return None


def divide(x, y):
    return validate_operations(x, y, lambda a, b: a / b)


def modulo(x, y):
    return validate_operations(x, y, lambda a, b: a % b)


def floor_division(x, y):
    return validate_operations(x, y, lambda a, b: a // b)


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': divide,
    'mod': modulo,
    'pow': lambda x, y: x ** y,
    'div': floor_division,
}

if __name__ == '__main__':
    first_num = validate_input()
    second_num = validate_input()

    operators_str = ', '.join(OPERATORS.keys())
    operation = input(f'Enter the operation ({operators_str}): ')

    while operation not in OPERATORS:
        print('Invalid operation. Please enter a valid operation.')
        operation = input(f'Enter the operation ({operators_str}): ')

    result = OPERATORS[operation](first_num, second_num)

    if result is not None:
        print(result)
