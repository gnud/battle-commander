import contextlib
from io import StringIO
import unittest

import app


class TestShips(unittest.TestCase):
    def setUp(self):
        self.board = app.Board()

    def test_destroyer(self):
        s = app.Destroyer(self.board)

        self.assertEqual(s.blocks, 4)
        self.assertNotEqual(s.board, None)

    def test_battle(self):
        s = app.Battle(self.board)

        self.assertEqual(s.blocks, 5)
        self.assertNotEqual(s.board, None)


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = app.Board()

    def test_create(self):
        self.assertNotEqual(self.board, None)

    def test_ships(self):
        self.assertEqual(len(self.board.ships), 2)

    @unittest.skip("not finished")
    def test_occupy_spot(self):
        pass

    def test_board(self):
        print(self.board.board)
        self.assertEqual(hasattr(self.board, 'board'), True)
        self.assertEqual(len(self.board.board), self.board.Y)
        self.assertEqual(len(self.board.board[0]), self.board.X)

    @unittest.skip("not finished")
    def test_reset(self):
        print(self.board.board)
        self.board.reset()
        print(self.board.board)

        self.assertNotEqual(self.board, None)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = app.Menu(None)

    def test_commands(self):
        commands = ['restart', 'exit', 'cheat', 'help']

        self.assertListEqual(list(self.menu.cmds.keys()), commands)


class TestGame(unittest.TestCase):
    def fake_start(self):
        pass

    def setUp(self):
        app._start_game = app.Game.start_game
        app.Game.start_game = self.fake_start
        self.game = app.Game()

    def test_banner(self):
        temp_stdout = StringIO()

        with contextlib.redirect_stdout(temp_stdout):
            self.game.draw_banner()

        output = temp_stdout.getvalue().strip()
        self.assertEqual("Let's play Battleship!", output)
