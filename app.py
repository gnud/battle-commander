#!/usr/bin/python3
import re
import string
import sys

horizontal_letters = range(1, 11)
vertical_letters = string.ascii_uppercase


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

    def reset(self):
        pass

    def calc_free_moves(self):
        return self.X * self.Y

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


class Player:
    def __init__(self):
        self.score = 0

    def reset(self):
        self.score = 0

    def print_invalid_err(self):
        print('Invalid input !')

    def validate_input(self, val):
        if len(val) < 2:
            self.print_invalid_err()
            return False

        try:
            self.char_letter, self.char_number = re.split('(\d+)', val)[:-1]
        except:
            self.print_invalid_err()
            return False

        if self.char_letter == '' or self.char_letter == False or self.char_letter == None or self.char_letter.upper().strip() not in vertical_letters:
            self.print_invalid_err()
            return False

        num = int(self.char_number) if self.char_number.isdigit() else None

        if num not in list(horizontal_letters):
            self.print_invalid_err()
            return False

        return True

    def parse_input(self, val):
        result = self.validate_input(val)

        if result is None:
            raise Exception('Invalid move!')

        return self.char_letter, self.char_number,


class Menu:
    def parse_input(self, cmd):
        if cmd in self.cmds:
            return self.cmds[cmd]

        return None

    def endgame_cmd(self):
        """end - End game."""

        self.game.endgame()

    def restart_game_cmd(self):
        """restart - Restart the game."""

        self.game.reset()

    def exit_app_cmd(self):
        """exit - Exit from the app."""

        self.game.endgame()
        sys.exit(0)

    def help_cmd(self):
        """help - app usage"""

        print('Usage:')
        cmds = ["%s" % (str(getattr(self, cmd).__doc__)) for cmd in dir(self) if '_cmd' in cmd]
        print('\n'.join(cmds))

    def __init__(self, game):
        self.game = game

        self.cmds = {
            'end': self.endgame_cmd,
            'restart': self.restart_game_cmd(),
            'exit': self.exit_app_cmd,
            'help': self.help_cmd,
        }


class Game:
    def __init__(self):
        self.game_state = True
        self.available_moves = 0
        self.position = -1

        self.board = Board()
        self.player = Player()
        self.menu = Menu(self)
        self.init_game()

    def endgame(self):
        self.game_over()

    def reset(self):
        self.game_state = True
        self.available_moves = 0
        self.position = -1

        self.board.reset()
        self.player.reset()

    def game_over(self):
        print('Game Over!')
        # TODO: print stats

    def process_move(self, moves):
        print('Doing action stub...')

    def parse_cmd(self, val):
        result = self.menu.parse_input(val)

        if result:
            result()

        if not result:
            moves = self.player.parse_input(val)

            if moves:
                self.process_move(moves)

    def input_loop(self):
        msg = '> '
        val = input(msg)

        try:
            while not self.parse_cmd(val):
                val = input(msg)
        except Exception as msg:
            print(msg)

        return val

    def main_loop(self):
        while self.game_state:
            self.input_loop()

            # Temporal code to simulate game over
            if self.available_moves == 0:
                self.game_state = False
                break

            self.available_moves -= 1
        else:
            self.game_over()

    def draw_banner(self):
        print("Let's play Battleship!")

    def init_game(self):
        # self.available_moves = self.board.calc_free_moves()
        self.available_moves = 5  # For debug

        # let's paint some staff, shall we
        self.draw_banner()
        self.board.render()

        # Load the main input system
        self.main_loop()


if __name__ == '__main__':
    Game()
