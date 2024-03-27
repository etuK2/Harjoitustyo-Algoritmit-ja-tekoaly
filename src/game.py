"""A module for implementing a Connect Four game"""

def create_board(rows, columns):
    """
    Luo pelilaudan annetujen rivien ja sarakkeiden määrän perusteella
    """
    board = [["  " for _ in range(columns)] for _ in range(rows)]
    return board

def place_piece(board, row, column, piece):
    """
    Asettaa pelinappulan halutulle paikalle
    """
    board[row][column] = piece

def next_free_row(board, rows, column):
    """
    Katsoo millä rivillä kyseisessä sarakkeessa on seuraava vapaa paikka
    """
    for i in range(rows-1, -1, -1):
        if board[i][column] == "  ":
            return i
    return None

def check_placement(board, column):
    """
    Tarkistaa onko läyttäjän antama syöte kelvollinen
    """
    return board[0][column] == "  "

def check_game_end(board, rows, columns, piece):
    """
    Tarkistaa onko peli päättynyt voitto siirtoon
    """
    # Tarkistaa tapahtuuko voitto pystysuunnassa
    for i in range(columns):
        for j in range(rows-3):
            if all(board[j+k][i] == piece for k in range(4)):
                return True
    # Tarkistaa tapahtuuko voitto vaakasuunnassa
    for i in range(columns-3):
        for j in range(rows):
            if all(board[j][i+k] == piece for k in range(4)):
                return True
    # Tarkistaa tapahtuuko voitto vinottaissuunnassa "/"
    for i in range(columns-3):
        for j in range(3, rows):
            if all(board[j-k][i+k] == piece for k in range(4)):
                return True
    # Tarkistaa tapahtuuko voitto vinottaissuunnassa "\"
    for i in range(3, columns):
        for j in range(3, rows):
            if all(board[j-k][i-k] == piece for k in range(4)):
                return True
    return False

def draw_board(board):
    """
    Piirtää pelilaudan tämänhetkisen tilan
    """
    for row in board:
        print(row)

def check_free_spaces(board, columns):
    """
    Tarkistaa onko pelilaudalla tyhjiä paikkoja
    """
    free_spaces = []
    for i in range(columns):
        if check_placement(board, i):
            free_spaces.append(i)
    return free_spaces
