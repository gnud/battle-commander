import string


class Board:
    def __init__(self):
        self.is_labels = True
        self.alphabet = string.ascii_uppercase
        self.nums = range(1, 11)
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


def init_game():
    board = Board()

    # starting the game and printing the board
    print("Let's play Battleship!")

    board.render()


if __name__ == '__main__':
    init_game()
