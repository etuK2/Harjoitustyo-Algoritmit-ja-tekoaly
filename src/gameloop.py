import game
import game_ai

rows = 6
columns = 7

player1_piece = "🔴"
player2_piece = "🟡"

player1_turn = 0
player2_turn = 1

turn = 0

board = game.create_board(rows, columns)
game_over = False

while not game_over:
    if len(game.check_free_spaces(board, columns)) == 0:
        game_over = True
        print("Tasapeli")

    if turn == player1_turn and not game_over:
        game.draw_board(board)
        column = int(input("Pelaaja 1 anna siirron sarake:"))-1
        if game.check_placement(board, column):
            row = game.next_free_row(board, rows, column)
            game.place_piece(board, row, column, player1_piece)
            if game.check_game_end(board, rows, columns, player1_piece):
                game_over = True
                game.draw_board(board)
                print("Pelaaja 1 voitti")
            turn += 1
        else:
            print("Anna kelvollinen siirto")
            pass

    if turn == player2_turn and not game_over:
        column, minimax_score = game_ai.minimax(board, 5, float('-inf'), float('inf'), True)
        
        if game.check_placement(board, column):
            row = game.next_free_row(board, rows, column)
            game.place_piece(board, row, column, player2_piece)
            if game.check_game_end(board, rows, columns, player2_piece):
                game_over = True
                game.draw_board(board)
                print("Pelaaja 2 voitti")
            turn -= 1