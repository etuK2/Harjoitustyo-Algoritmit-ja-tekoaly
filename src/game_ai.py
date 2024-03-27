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

def minimax(board, depth, alpha, beta, player, move_count):

    if depth == 0 or move_count == 42:
        return (None, board_value(board, player2_piece))
    
    if player:
        value = float('-inf')
        column = random.choice(game.check_free_spaces(board, columns))
        
        for i in game.check_free_spaces(board, columns):
            row = game.next_free_row(board, rows, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player2_piece)
            
            if game.check_game_end(copy, rows, columns, player2_piece):
                return (i, 1000)
            
            new_value = minimax(copy, depth - 1, alpha, beta, False, move_count + 1)[1]
            if new_value > value:
                value = new_value
                column = i
            
            alpha = max(value, alpha)
            if alpha >= beta:
                break
        
        return column, value
    
    else:
        value = float('inf')
        column = random.choice(game.check_free_spaces(board, columns))
        
        for i in game.check_free_spaces(board, columns):
            row = game.next_free_row(board, rows, i)
            copy = [row[:] for row in board]
            game.place_piece(copy, row, i, player1_piece)
            
            if game.check_game_end(copy, rows, columns, player1_piece):
                return (i, -1000)
            
            new_value = minimax(copy, depth - 1, alpha, beta, True, move_count + 1)[1]
            if new_value < value:
                value = new_value
                column = i
            
            beta = min(value, beta)
            if alpha >= beta:
                break
        
        return column, value