"""Test cases for Connect Four game AI functions"""

import unittest
from game_ai import check_value, board_value, minimax, iterative_deepening

class TestGameAI(unittest.TestCase):
    """Test cases for Connect Four game AI functions"""

    def test_check_value(self):
        """
        Test check_value function
        """
        player1_piece = 1
        player2_piece = 2
        piece = 1
        area = [1, 1, 1, 1]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 100)
        area = [1, 1, 0, 1]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 5)
        area = [1, 0, 0, 1]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), 2)
        area = [2, 2, 0, 2]
        self.assertEqual(check_value(area, piece, player1_piece, player2_piece), -4)

    def test_board_value(self):
        """
        Test board_value function
        """
        player1_piece = 1
        player2_piece = 2
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        piece = 1
        self.assertEqual(board_value(board, piece, player1_piece, player2_piece), 0)

    def test_minimax(self):
        """
        Test minimax function
        """
        player1_piece = 1
        player2_piece = 2
        move_count = 1
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]
        ]
        depth = 3
        alpha = float("-inf")
        beta = float("inf")
        player = True
        move_count = 7
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece, hash_map={}), (3, 10))
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [2, 2, 2, 0, 1, 1, 1]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece, hash_map={}), (3, 1000))
        move_count = 5
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2],
            [1, 1, 1, 0, 0, 0, 2]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                move_count, player1_piece, player2_piece, hash_map={}), (3, 14))
        move_count = 42
        board = [
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, player,
                                  move_count, player1_piece, player2_piece, hash_map={}), (None, 0))

    def test_iterative_deepening(self):
        """
        Test iterative_deepening function
        """
        player1_piece = 1
        player2_piece = 2
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
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
        board = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 1, 2, 2, 2, 0, 0],
            [0, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0]
        ]
        max_depth = 10
        time_limit = 2
        # Voitto ai:lle 9 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 3] ja [Pelaaja(nappula 1): 5]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 2)
        board = [
            [0, 0, 2, 1, 1, 0, 0],
            [0, 1, 2, 2, 2, 0, 0],
            [0, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0]
        ]
        max_depth = 9
        # Voitto ai:lle 8 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 2] ja [Pelaaja(nappula 1): 1]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 1)
        board = [
            [0, 2, 2, 1, 1, 0, 0],
            [0, 1, 2, 2, 2, 0, 0],
            [1, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 0, 0],
            [2, 2, 1, 2, 1, 0, 0]
        ]
        max_depth = 8
        # Voitto ai:lle 7 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 6] ja [Pelaaja(nappula 1): 6]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 5)
        board = [
            [0, 2, 2, 1, 1, 0, 0],
            [0, 1, 2, 2, 2, 0, 0],
            [1, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 0, 0],
            [1, 1, 2, 1, 1, 1, 0],
            [2, 2, 1, 2, 1, 2, 0]
        ]
        max_depth = 7
        # Voitto ai:lle 6 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 6] ja [Pelaaja(nappula 1): 1]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 5)
        board = [
            [0, 2, 2, 1, 1, 0, 0],
            [1, 1, 2, 2, 2, 0, 0],
            [1, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 2, 0],
            [1, 1, 2, 1, 1, 1, 0],
            [2, 2, 1, 2, 1, 2, 0]
        ]
        max_depth = 6
        # Voitto ai:lle 5 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 1] ja [Pelaaja(nappula 1): 7]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 0)
        board = [
            [2, 2, 2, 1, 1, 0, 0],
            [1, 1, 2, 2, 2, 0, 0],
            [1, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 2, 0],
            [1, 1, 2, 1, 1, 1, 0],
            [2, 2, 1, 2, 1, 2, 1]
        ]
        max_depth = 5
        # Voitto ai:lle 4 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 7] ja [Pelaaja(nappula 1): 7]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 6)
        board = [
            [2, 2, 2, 1, 1, 0, 0],
            [1, 1, 2, 2, 2, 0, 0],
            [1, 2, 2, 1, 1, 0, 0],
            [2, 1, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2],
            [2, 2, 1, 2, 1, 2, 1]
        ]
        max_depth = 4
        # Voitto ai:lle 3 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 7] ja [Pelaaja(nappula 1): 7]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 6)
        board = [
            [2, 2, 2, 1, 1, 0, 0],
            [1, 1, 2, 2, 2, 0, 1],
            [1, 2, 2, 1, 1, 0, 2],
            [2, 1, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2],
            [2, 2, 1, 2, 1, 2, 1]
        ]
        max_depth = 3
        # Voitto ai:lle 2 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 7] ja [Pelaaja(nappula 1): 6]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 6)
        board = [
            [2, 2, 2, 1, 1, 0, 2],
            [1, 1, 2, 2, 2, 0, 1],
            [1, 2, 2, 1, 1, 1, 2],
            [2, 1, 1, 2, 2, 2, 1],
            [1, 1, 2, 1, 1, 1, 2],
            [2, 2, 1, 2, 1, 2, 1]
        ]
        max_depth = 3
        # Voitto ai:lle 1 liikkeenpäässä siirroilla sarakkeisiin [Ai(nappula 2): 6]
        self.assertEqual(iterative_deepening(board, max_depth, alpha, beta, player, move_count,
                                              time_limit, player1_piece, player2_piece), 5)