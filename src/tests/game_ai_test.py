"""Test cases for Connect Four game AI functions"""

import unittest
from game_ai import check_value, board_value, minimax, iterative_deepening

class TestGameAI(unittest.TestCase):
    """Test cases for Connect Four game AI functions"""

    def test_check_value(self):
        """
        Test check_value function
        """
        player1_piece = "X"
        player2_piece = "O"
        piece = "X"
        area = ["X", "X", "X", "X"]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 100)
        area = ["X", "X", "  ", "X"]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 5)
        area = ["X", "  ", "  ", "X"]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 2)
        area = ["O", "O", "  ", "O"]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), -4)

    def test_board_value(self):
        """
        Test board_value function
        """
        player1_piece = "X"
        player2_piece = "O"
        board = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
        ]
        piece = "X"
        self.assertEqual(board_value(board, piece, player1_piece, player2_piece), 0)

    def test_minimax(self):
        """
        Test minimax function
        """
        player1_piece = "X"
        player2_piece = "O"
        move_count = 1
        board = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "X", "  ", "  ", "  "]
        ]
        depth = 3
        alpha = float("-inf")
        beta = float("inf")
        player = True
        move_count = 7
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece), (3, 10))
        board = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "X"],
            ["O", "O", "O", "  ", "X", "X", "X"]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece), (3, 1000))
        move_count = 5
        board = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "O"],
            ["X", "X", "X", "  ", "  ", "  ", "O"]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece), (3, 14))
        move_count = 42
        board = [
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O"],
            ["X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X"]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece), (None, 0))

    def test_iterative_deepening(self):
        """
        Test iterative_deepening function
        """
        player1_piece = "X"
        player2_piece = "O"
        board = [
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  "]
        ]
        max_depth = 3
        alpha = float("-inf")
        beta = float("inf")
        player = True
        move_count = 0
        time_limit = 2
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 3)
        max_depth = 100000
        time_limit = 1
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 3)
