def determine_square_color(position):
    return 'black' if (ord(position[0]) + int(position[1])) % 2 == 0 else 'white'


def validate_input(position):
    return len(position) == 2 and \
           position[0] in 'abcdefgh' and \
           position[1].isdigit() and \
           1 <= int(position[1]) <= 8


if __name__ == '__main__':
    position = input('Enter the position of the chess piece (e.g., a1): ')
    while not validate_input(position):
        print('Invalid position. Please try again.')
        position = input('Enter the position of the chess piece (e.g., a1): ')

    color = determine_square_color(position)
    print('The square has color:', color)
