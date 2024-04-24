"""Connect Four AI Module"""

import random
import time
import game

ROWS = 6
COLUMNS = 7

def check_value(area, piece, player1_piece, player2_piece):
    """
    Laskee lähellä olevien nappuloiden arvot
    """
    opponent_piece = player1_piece if piece == player2_piece else player2_piece
    value = 0

    if area.count(piece) == 4:
        value += 100
    elif area.count(piece) == 3 and area.count("  ") == 1:
        value += 5
    elif area.count(piece) == 2 and area.count("  ") == 2:
        value += 2

    if area.count(opponent_piece) == 3 and area.count("  ") == 1:
        value -= 4

    return value


def board_value(board, piece, player1_piece, player2_piece):
    """
    Laskee pelilaudan arvon
    """
    value = 0
    center_column = [board[i][COLUMNS // 2] for i in range(ROWS)]
    center_count = center_column.count(piece)
    value += center_count * 5

    # Pystysuuntainen arvo
    for i in range(COLUMNS):
        column = [board[k][i] for k in range(ROWS)]
        for j in range(ROWS - 3):
            area = column[j : j + 4]
            value += check_value(area, piece, player1_piece, player2_piece)

    # Vaakasuuntainen arvo
    for i in range(ROWS):
        row = board[i]
        for j in range(COLUMNS - 3):
            area = row[j : j + 4]
            value += check_value(area, piece, player1_piece, player2_piece)

    # Vinottaissuuntainen arvo suunnassa "/"
    for i in range(3, ROWS):
        for j in range(COLUMNS - 3):
            area = [board[i - k][j + k] for k in range(4)]
            value += check_value(area, piece, player1_piece, player2_piece)

    # Vinottaissuuntainen arvo suunnassa "\"
    for i in range(3, ROWS):
        for j in range(3, COLUMNS):
            area = [board[i - k][j - k] for k in range(4)]
            value += check_value(area, piece, player1_piece, player2_piece)

    return value


def minimax(board, depth, alpha, beta, player, move_count, player1_piece, player2_piece, hash_map): #pylint: disable=too-many-arguments, too-many-return-statements, too-many-branches
    """
    Minimax-algoritmi alfa-beeta-karsinnalla
    """
    if move_count == 42:
        return None, 0

    if depth == 0:
        return None, board_value(board, player2_piece, player1_piece, player2_piece)
    
    ordered_columns = sorted(game.check_free_spaces(board, COLUMNS), key=lambda x: abs(x - COLUMNS // 2))

    if player: #pylint: disable=no-else-return
        value = float("-inf")
        column = random.choice(game.check_free_spaces(board, COLUMNS))

        board_key = str(board)
        best_move = hash_map.get(board_key)
        if best_move is not None:
            ordered_columns.remove(best_move)
            ordered_columns.insert(0, best_move)

        for i in ordered_columns:
            row = game.next_free_row(board, ROWS, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player2_piece)

            if game.check_game_end(copy, ROWS, COLUMNS, player2_piece):
                return i, 1000

            new_value = minimax(copy, depth - 1, alpha, beta, False,
                                 move_count + 1, player1_piece, player2_piece, hash_map)[1]
            if new_value > value:
                value = new_value
                column = i

            alpha = max(value, alpha)
            if alpha >= beta:
                break
        
        hash_map[board_key] = column
        return column, value

    else:
        value = float("inf")
        column = random.choice(game.check_free_spaces(board, COLUMNS))

        board_key = str(board)
        best_move = hash_map.get(board_key)
        if best_move is not None:
            ordered_columns.remove(best_move)
            ordered_columns.insert(0, best_move)

        for i in ordered_columns:
            row = game.next_free_row(board, ROWS, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player1_piece)

            if game.check_game_end(copy, ROWS, COLUMNS, player1_piece):
                return i, -1000

            new_value = minimax(copy, depth - 1, alpha, beta, True,
                                 move_count + 1, player1_piece, player2_piece, hash_map)[1]
            if new_value < value:
                value = new_value
                column = i

            beta = min(value, beta)
            if alpha >= beta:
                break
        
        hash_map[board_key] = column
        return column, value

def iterative_deepening(board, max_depth, aplha, beta, player, move_count, time_limit, player1_piece, player2_piece): #pylint: disable=too-many-arguments, line-too-long
    """
    Iteratiivinen syveneminen minimax-algoritmiin
    """
    hash_map = {}
    start_time = time.time()
    best_move = None
    for depth in range(1, max_depth+1):
        best_move, _ = minimax(board, depth, aplha, beta, player,
                           move_count, player1_piece, player2_piece, hash_map)
        if time.time() - start_time > time_limit:
            break
    return best_move