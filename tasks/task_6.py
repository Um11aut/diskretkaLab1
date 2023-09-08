chess_board = []

for i in range(8):
    row = []
    for j in range(8):
        row.append(" ")
    chess_board.append(row)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chess_board[i][j] = "0" 
        else:
            chess_board[i][j] = "1"

def check_for_white(x: int, y: int):
    if chess_board[7-x][y-1] == "0":
        return True
    else:
        return False