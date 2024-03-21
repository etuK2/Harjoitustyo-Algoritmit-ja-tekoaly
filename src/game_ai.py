import game
import random

rows = 6
columns = 7

player1_piece = "🔴"
player2_piece = "🟡"

#Katsoo milloin peli loppuu joko voittoon tai tasapeliin
def game_over_checker(board):
    return game.check_game_end(board, rows, columns, player1_piece) or game.check_game_end(board, rows, columns, player2_piece) or len(game.check_free_spaces(board, columns)) == 0

#Laskee arvoja lähekkäin oleville paloille, pisteitä saa enemmän mitä lähempänä voittoa palat ovat
def check_value(area, piece):
    opponent_piece = player1_piece

    if piece == player1_piece:
        opponent_piece = player2_piece
    
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

#Kertoo pelilaudan arvon siirron jälkeen
def board_value(board, piece):
    value = 0
    center_column = [board[i][columns//2] for i in range(rows)]
    center_count = center_column.count(piece)
    value += center_count*5

    #Kertoo arvon pystysuunnassa
    for i in range(columns):
        column = [board[k][i] for k in range(rows)]
        for j in range(rows-3):
            area = column[j:j+4]
            value += check_value(area, piece)
    
    #Kertoo arvon vaakasuunnassa
    for i in range(rows):
        row = board[i]
        for j in range(columns-3):
            area = row[j:j+4]
            value += check_value(area, piece)
    
    #Kertoo arvon vinoittais / suunnassa
    for i in range(3,rows):
        for j in range(columns-3):
            area = [board[i-k][j+k] for k in range(4)]
            value += check_value(area, piece)

    #Kertoo arvon vinoittais \ suunnassa
    for i in range(3,rows):
        for j in range(3,columns):
            area = [board[i-k][j-k] for k in range(4)]
            value += check_value(area, piece)    

    return value

def minimax(board, depth, aplha, beta, player):

    game_over_value = game_over_checker(board)

    free_spaces = game.check_free_spaces(board, columns)

    if depth == 0 or game_over_value:
        if game_over_value:
            if game.check_game_end(board, rows, columns, player1_piece):
                return (None, -1000)
            
            elif game.check_game_end(board, rows, columns, player2_piece):
                return (None, 1000)
            
            else:
                return (None, 0)
        
        else:
            return (None, board_value(board, player2_piece))
    

    if player:
        value = float('-inf')

        column = random.choice(free_spaces)

        for i in free_spaces:
            row = game.next_free_row(board, rows, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player2_piece)

            new_value = minimax(copy, depth-1, aplha, beta, False)[1]
            if new_value > value:
                value = new_value
                column = i

            aplha = max(value, aplha)
            if aplha >= beta:
                break
        
        return column, value
    
    if player == False:
        value = float('inf')

        column = random.choice(free_spaces)

        for i in free_spaces:
            row = game.next_free_row(board, rows, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player1_piece)

            new_value = minimax(copy, depth-1, aplha, beta, True)[1]
            if new_value < value:
                value = new_value
                column = i

            beta = min(value, beta)
            if aplha >= beta:
                break
        
        return column, value