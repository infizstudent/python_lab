def determine_square_color(chess_position):
    return 'black' if (ord(chess_position[0]) + int(chess_position[1])) % 2 == 0 else 'white'


def validate_input(chess_position):
    return len(chess_position) == 2 and \
           chess_position[0] in 'abcdefgh' and \
           chess_position[1].isdigit() and \
           1 <= int(chess_position[1]) <= 8


if __name__ == '__main__':
    position = input('Enter the position of the chess piece (e.g., a1): ')
    while not validate_input(position):
        print('Invalid position. Please try again.')
        position = input('Enter the position of the chess piece (e.g., a1): ')

    color = determine_square_color(position)
    print('The square has color:', color)
