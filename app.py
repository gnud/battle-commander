#!/usr/bin/python3
import re
import string

horizontal_letters = range(1, 11)
vertical_letters = string.ascii_uppercase

game_state = True

class Board:
    def __init__(self):
        self.is_labels = True
        self.alphabet = vertical_letters
        self.nums = horizontal_letters
        self.cloaked_symbol = "."
        self.X = 10
        self.Y = 10

        self.board = []

        self.build_board()

    def build_board(self):
        for x in range(self.X):
            self.board.append([self.cloaked_symbol] * self.Y)

    def render(self):
        self.render_h_labels()

        for idx, row in enumerate(self.board):
            self.render_v_labels(idx)
            print(" ".join(row))

    def render_v_labels(self, cur_letter):
        if not self.is_labels:
            return

        print('%s ' % self.alphabet[cur_letter], end='')

    def render_h_labels(self):
        if not self.is_labels:
            return

        print(' ', end=' ')
        print(' '.join(str(x) for x in self.nums), end=' ')
        print('')

    def reveal(self):
        """Show ship position command - aids in debugging"""
        pass

    def construct_battleship(self):
        sqrs = 5

    def construct_destoyer(self):
        sqrs = 4


def print_invalid_err():
    print('Invalid input !')


def validate_input(val):
    if len(val) < 2:
        print_invalid_err()
        return False

    try:
        char_a, char_b = re.split('(\d+)', val)[:-1]
    except:
        print_invalid_err()
        return False

    if char_a == '' or char_a == False or char_a == None or char_a.upper().strip() not in vertical_letters:
        print_invalid_err()
        return False

    num = int(char_b) if char_b.isdigit() else None

    if num not in list(horizontal_letters):
        print_invalid_err()
        return False

    return True


def render_input():
    msg = 'Enter position> '
    val = input(msg)

    try:
        while not validate_input(val):
            val = input(msg)
    except Exception as msg:
        print(msg)

    return val


def game_over():
    print('Game Over!')
    # TODO: print stats


def main_loop():
    global game_state
    a = 0
    while game_state:
        val = render_input()

        # Temporal code to simulate game over
        if a == 3:
            game_state = False
        a += 1
    else:
        game_over()


def init_game():
    board = Board()

    # starting the game and printing the board
    print("Let's play Battleship!")

    board.render()
    main_loop()


if __name__ == '__main__':
    init_game()
