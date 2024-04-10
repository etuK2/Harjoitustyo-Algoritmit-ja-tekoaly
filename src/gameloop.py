"""Module for running the game loop."""

import game
import game_ai

ROWS = 6
COLUMNS = 7

PLAYER1_PIECE = "🔴"
PLAYER2_PIECE = "🟡"

PLAYER1_TURN = 0
PLAYER2_TURN = 1

MOVE_COUNT = 0
TURN = 0

BOARD = game.create_board(ROWS, COLUMNS)
GAME_OVER = False

while not GAME_OVER:
    if len(game.check_free_spaces(BOARD, COLUMNS)) == 0:
        GAME_OVER = True
        print("Tasapeli")

    if TURN == PLAYER1_TURN and not GAME_OVER:
        COLUMN = ""
        game.draw_board(BOARD)
        while isinstance(COLUMN, int) is False:
            try:
                COLUMN = int(input("Pelaaja 1 anna sarakkeen numero:")) - 1
            except ValueError:
                COLUMN = 999
        if 0 <= COLUMN <= 6 and game.check_placement(BOARD, COLUMN):
            row = game.next_free_row(BOARD, ROWS, COLUMN)
            game.place_piece(BOARD, row, COLUMN, PLAYER1_PIECE)
            if game.check_game_end(BOARD, ROWS, COLUMNS, PLAYER1_PIECE):
                GAME_OVER = True
                game.draw_board(BOARD)
                print("Pelaaja 1 voitti")
            TURN += 1
        else:
            print("Syötteen pitää olla luku väliltä 1-7")

    if TURN == PLAYER2_TURN and not GAME_OVER:
        COLUMN = game_ai.iterative_deepening(
            BOARD, 10, float('-inf'), float('inf'), True, MOVE_COUNT, 2)

        if game.check_placement(BOARD, COLUMN):
            row = game.next_free_row(BOARD, ROWS, COLUMN)
            game.place_piece(BOARD, row, COLUMN, PLAYER2_PIECE)
            if game.check_game_end(BOARD, ROWS, COLUMNS, PLAYER2_PIECE):
                GAME_OVER = True
                game.draw_board(BOARD)
                print("Pelaaja 2 voitti")
            TURN -= 1
