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

def is_queen_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    else:
        return False
    
