import unittest
from game import create_board, place_piece, next_free_row, check_placement, check_game_end, draw_board, check_free_spaces

class TestConnectFour(unittest.TestCase):

    def test_create_board(self):
        rows = 6
        columns = 7
        board = create_board(rows, columns)
        self.assertEqual(len(board), rows)
        for row in board:
            self.assertEqual(len(row), columns)
            for cell in row:
                self.assertEqual(cell, "  ")

    def test_place_piece(self):
        board = [["  ", "  "], ["  ", "  "]]
        place_piece(board, 0, 0, "X")
        self.assertEqual(board[0][0], "X")

    def test_next_free_row(self):
        board = [["X", "  "], ["X", "O"]]
        rows = 2
        column = 1
        self.assertEqual(next_free_row(board, rows, column), 0)

    def test_check_placement(self):
        board = [["  ", "O"], ["  ", "X"]]
        self.assertTrue(check_placement(board, 0))
        self.assertFalse(check_placement(board, 1))

    def test_check_game_end(self):
        board = [["X", "  ", "  ", "  "],
                 ["X", "O", "  ", "  "],
                 ["X", "O", "  ", "  "],
                 ["X", "O", "  ", "  "]]
        rows = 4
        columns = 4
        piece = "X"
        self.assertTrue(check_game_end(board, rows, columns, piece))
        board = [["  ", "  ", "  ", "  "],
                 ["X", "O", "  ", "  "],
                 ["X", "X", "X", "X"],
                 ["X", "O", "O", "O"]]
        rows = 4
        columns = 4
        piece = "X"
        self.assertTrue(check_game_end(board, rows, columns, piece))
        board = [["  ", "  ", "  ", "X"],
                 ["  ", "O", "X", "O"],
                 ["X", "X", "O", "O"],
                 ["X", "O", "O", "O"]]
        rows = 4
        columns = 4
        piece = "X"
        self.assertTrue(check_game_end(board, rows, columns, piece))
        board = [["X", "  ", "  ", "  "],
                 ["O", "X", "  ", "  "],
                 ["X", "O", "X", "O"],
                 ["X", "O", "O", "X"]]
        rows = 4
        columns = 4
        piece = "X"
        self.assertTrue(check_game_end(board, rows, columns, piece))
        board = [["  ", "  ", "  ", "  "],
                 ["  ", "O", "X", "O"],
                 ["X", "X", "O", "O"],
                 ["X", "O", "O", "O"]]
        rows = 4
        columns = 4
        piece = "X"
        self.assertFalse(check_game_end(board, rows, columns, piece))
        

    def test_check_free_spaces(self):
        board = [["  ", "  ", "  "], ["  ", "X", "  "], ["X", "O", "  "]]
        columns = 3
        print(check_free_spaces(board, columns))
        self.assertEqual(check_free_spaces(board, columns), [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
