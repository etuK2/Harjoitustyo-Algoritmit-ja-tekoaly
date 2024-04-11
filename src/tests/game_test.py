"""Test cases for Connect Four game functions"""

import unittest
from game import (create_board, place_piece, next_free_row,
                  check_placement, check_game_end, check_free_spaces)

class TestConnectFour(unittest.TestCase):
    """Test cases for Connect Four game functions"""

    def test_create_board(self):
        """
        Test create_board function
        """
        rows, columns = 6, 7
        board = create_board(rows, columns)
        self.assertEqual(len(board), rows)
        self.assertEqual(len(board[0]), columns)

    def test_place_piece(self):
        """
        Test place_piece function
        """
        board = [["  ", "  "], ["  ", "  "]]
        place_piece(board, 0, 0, "X")
        self.assertEqual(board[0][0], "X")

    def test_next_free_row(self):
        """
        Test next_free_row function
        """
        board = [["X", "  "], ["X", "O"]]
        rows = 2
        column = 1
        self.assertEqual(next_free_row(board, rows, column), 0)
        board = [["X", "O"], ["X", "O"]]
        rows = 2
        column = 1
        self.assertEqual(next_free_row(board, rows, column), None)

    def test_check_placement(self):
        """
        Test check_placement function
        """
        board = [["  ", "O"], ["  ", "X"]]
        self.assertTrue(check_placement(board, 0))
        self.assertFalse(check_placement(board, 1))

    def test_check_game_end(self):
        """
        Test check_game_end function
        """
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
        """
        Test check_free_spaces function
        """
        board = [["  ", "  ", "  "], ["  ", "X", "  "], ["X", "O", "  "]]
        columns = 3
        self.assertEqual(check_free_spaces(board, columns), [0, 1, 2])
        board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        columns = 3
        self.assertEqual(check_free_spaces(board, columns), [])
