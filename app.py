#!/usr/bin/python3
import random
import re
import string
import sys

horizontal_letters = range(1, 11)
vertical_letters = string.ascii_uppercase


class Ship:
    def __init__(self, board):
        self.board = board

        self.x = 0
        self.y = 0

        self.blocks_data = {}

        self.randomize()

    def randomize(self):
        def fill_data():
            block_available = row[random_y:random_y + self.blocks]
            for c in block_available:
                if c[1]:
                    break
            else:
                self.blocks_data = { b[0]: True for b in block_available}
                print(self.blocks_data)

                return True

        for i in range(0, self.board.Y):
            row = self.board.find_rows_with_n_free(vertical_letters[i])

            random_y = random.randrange(self.board.Y)

            if random_y <= self.board.X / 2:
                if not self.blocks + random_y > self.board.X:
                    if fill_data():
                        break

            if random_y > self.board.X / 2:
                if not self.blocks <= (self.board.X / 2):
                    if fill_data():
                        break

        for c in self.blocks_data.keys():
            self.board.occupy_spot(c)

        print(self.blocks_data.keys())

    def check(self, point):
        try:
            if (point in self.blocks_data):
                return True
        except:
            return False

    def get_position(self):
        return self.x, self.y,


class Battle(Ship):
    def __init__(self, board):
        self.blocks = 5
        self.name = 'Battle ship'
        self.board = board

        super(Battle, self).__init__(board)


class Destroyer(Ship):
    def __init__(self, board):
        self.blocks = 4
        self.name = 'Destroyer ship'
        self.board = board

        super(Destroyer, self).__init__(board)


class Board:
    def __init__(self):
        self.is_labels = True
        self.alphabet = vertical_letters
        self.nums = horizontal_letters
        self.cloaked_symbol = "."
        self.ship_char = '='
        self.X = 10
        self.Y = 10
        self.board_map = {}

        self.board = []

        self.build_board()

        self.ships = [
            Battle(self),
            Destroyer(self)
        ]

    def is_ship_in_sight(self, point):
        if(self.board_map[point]):
            return True
        return False

    def all_free_spots(self, label):
        is_free = len([l for l in self.board_map.keys() if l[0] == label]) > 0

        if is_free:
            return is_free

        a = [s.blocks_data for s in self.ships]

    def reset(self):
        pass

    def calc_free_moves(self):
        return self.X * self.Y

    def build_board(self):
        self.board_map = {"%s%s" % (v, h): False for v in vertical_letters[:10] for h in horizontal_letters}

        for x in range(self.X):
            self.board.append([self.cloaked_symbol] * self.Y)

    def occupy_spot(self, area):
        self.board_map[area] = True

    def is_spot_free(self, spot):
        if self.board_map[spot[0].upper()]:
            return True
        return False

    def find_rows_with_n_free(self, n):
        row = [(key, value) for key, value in self.board_map.items() if n in key.upper()]

        return row

    def render(self, cheat=False):
        self.render_h_labels()

        for idx, row in enumerate(self.board):
            self.render_v_labels(idx)

            if cheat:
                for idx_c, c in enumerate(row):
                    x, y = idx_c, idx
                    if self.is_ship_in_sight('%s%s' %(self.alphabet[idx], idx_c + 1)):
                        row[idx_c] = self.ship_char

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

        self.render(True)

    def construct_battleship(self):
        sqrs = 5

    def construct_destoyer(self):
        sqrs = 4

    def char_to_position(self, char):
        return vertical_letters.index(char.upper())

    def hit(self, position):
        letter, x_pos = position

        label = '%s%s' % (letter, x_pos)

        is_hit = self.is_spot_free([label])

        if is_hit:
            print('bang!')
        if not is_hit:
            print('Missed! - Sorry.')


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

    def cheat_cmd(self):
        """cheat - Reveal enemy'e ships."""

        self.game.cheat()

    def help_cmd(self):
        """help - app usage"""

        print('Usage:')
        cmds = ["%s" % (str(getattr(self, cmd).__doc__)) for cmd in dir(self) if '_cmd' in cmd]
        print('\n'.join(cmds))

    def __init__(self, game):
        self.game = game

        self.cmds = {
            'end': self.endgame_cmd,
            'restart': self.restart_game_cmd,
            'exit': self.exit_app_cmd,
            'cheat': self.cheat_cmd,
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

    def cheat(self):
        self.board.reveal()

    def game_over(self):
        print('Game Over!')
        # TODO: print stats

    def process_move(self, moves):
        self.board.hit(moves)


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
