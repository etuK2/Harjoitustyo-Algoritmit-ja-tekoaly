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
        game.draw_board(BOARD)
        column = int(input("Pelaaja 1 anna siirron sarake:")) - 1
        if game.check_placement(BOARD, column):
            row = game.next_free_row(BOARD, ROWS, column)
            game.place_piece(BOARD, row, column, PLAYER1_PIECE)
            if game.check_game_end(BOARD, ROWS, COLUMNS, PLAYER1_PIECE):
                GAME_OVER = True
                game.draw_board(BOARD)
                print("Pelaaja 1 voitti")
            TURN += 1
        else:
            print("Anna kelvollinen siirto")

    if TURN == PLAYER2_TURN and not GAME_OVER:
        column, _ = game_ai.minimax(BOARD, 5, float('-inf'), float('inf'), True, MOVE_COUNT)

        if game.check_placement(BOARD, column):
            row = game.next_free_row(BOARD, ROWS, column)
            game.place_piece(BOARD, row, column, PLAYER2_PIECE)
            if game.check_game_end(BOARD, ROWS, COLUMNS, PLAYER2_PIECE):
                GAME_OVER = True
                game.draw_board(BOARD)
                print("Pelaaja 2 voitti")
            TURN -= 1
