"""Connect Four AI Module"""

import random
import game

ROWS = 6
COLUMNS = 7

PLAYER1_PIECE = "🔴"
PLAYER2_PIECE = "🟡"

def check_value(area, piece):
    """
    Laskee lähellä olevien nappuloiden arvot
    """
    opponent_piece = PLAYER1_PIECE if piece == PLAYER2_PIECE else PLAYER2_PIECE
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


def board_value(board, piece):
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
            value += check_value(area, piece)

    # Vaakasuuntainen arvo
    for i in range(ROWS):
        row = board[i]
        for j in range(COLUMNS - 3):
            area = row[j : j + 4]
            value += check_value(area, piece)

    # Vinottaissuuntainen arvo suunnassa "/"
    for i in range(3, ROWS):
        for j in range(COLUMNS - 3):
            area = [board[i - k][j + k] for k in range(4)]
            value += check_value(area, piece)

    # Vinottaissuuntainen arvo suunnassa "\"
    for i in range(3, ROWS):
        for j in range(3, COLUMNS):
            area = [board[i - k][j - k] for k in range(4)]
            value += check_value(area, piece)

    return value


def minimax(board, depth, alpha, beta, player, move_count): #pylint: disable=too-many-arguments
    """
    Minimax-algoritmi alfa-beeta-karsinnalla
    """
    if depth == 0 or move_count == 42:
        return None, board_value(board, PLAYER2_PIECE)

    if player: #pylint: disable=no-else-return
        value = float("-inf")
        column = random.choice(game.check_free_spaces(board, COLUMNS))

        for i in game.check_free_spaces(board, COLUMNS):
            row = game.next_free_row(board, ROWS, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, PLAYER2_PIECE)

            if game.check_game_end(copy, ROWS, COLUMNS, PLAYER2_PIECE):
                return i, 1000

            new_value = minimax(copy, depth - 1, alpha, beta, False, move_count + 1)[1]
            if new_value > value:
                value = new_value
                column = i

            alpha = max(value, alpha)
            if alpha >= beta:
                break

        return column, value

    else:
        value = float("inf")
        column = random.choice(game.check_free_spaces(board, COLUMNS))

        for i in game.check_free_spaces(board, COLUMNS):
            row = game.next_free_row(board, ROWS, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, PLAYER1_PIECE)

            if game.check_game_end(copy, ROWS, COLUMNS, PLAYER1_PIECE):
                return i, -1000

            new_value = minimax(copy, depth - 1, alpha, beta, True, move_count + 1)[1]
            if new_value < value:
                value = new_value
                column = i

            beta = min(value, beta)
            if alpha >= beta:
                break

        return column, value
