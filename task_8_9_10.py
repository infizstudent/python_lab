from itertools import product


def determine_square_color(chess_position):
    return 'black' if (ord(chess_position[0]) + int(chess_position[1])) % 2 == 0 else 'white'


def validate_input(chess_position):
    input_position = input(chess_position)
    while input_position not in (''.join(i) for i in product('abcdefgh', '12345678')):
        print('Invalid position. Please try again.')
        input_position = input(chess_position)
    return input_position


if __name__ == '__main__':
    position = validate_input('Enter the position of the chess piece (e.g., a1): ')
    color = determine_square_color(position)
    print('The square has color:', color)
