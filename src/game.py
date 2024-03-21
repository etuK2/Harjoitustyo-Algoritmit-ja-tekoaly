def create_board(rows, columns):
    board = [["  " for _ in range(columns)] for _ in range(rows)]
    return board

def place_piece(board, row, column, piece):
    board[row][column] = piece

#Katsoo millä rivillä kyseisessä sarakkeessa on seuraava vapaa paikka
def next_free_row(board, rows, column):
    for i in range(rows-1,-1,-1):
        if board[i][column] == "  ":
            return i

#Tarkistaa onko läyttäjän antama syöte kelvollinen
def check_placement(board, column):
    return board[0][column] == "  "


def check_game_end(board, rows, columns, piece):
    #Katsoo onko 4 samaa nappulaa päällekkäin
    for i in range(columns):
        for j in range(rows-3):
            if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
                return True
    #Katsoo onko 4 samaa nappulaa vierekkäin
    for i in range(columns-3):
        for j in range(rows):
            if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
                return True
    #Katsoo onko 4 samaa nappulaa vinottain vierekkäin suunnassa /
    for i in range(columns-3):
        for j in range(3,rows):
            if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
                return True
    #Katsoo onko 4 samaa nappulaa vinottain vierekkäin suunnassa \
    for i in range(3,columns):
        for j in range(3,rows):
            if board[j][i] == piece and board[j-1][i-1] == piece and board[j-2][i-2] == piece and board[j-3][i-3] == piece:
                return True

def draw_board(board):
    for i in board:
        print(i)

#Tarkistaa onko pelilaudalla tyhjiä paikkoja
def check_free_spaces(board, columns):
    free_spaces = []
    for i in range(columns):
        if check_placement(board, i) == True:
            free_spaces.append(i)
    return free_spaces
