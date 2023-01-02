board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(b):

    for row in range (len(b)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        
        for col in range(len(b[row])):
            if col % 3 == 0 and col != 0:
                print("| ", end='')
            if col == 8:
                print(b[row][col])
            else:
                print(str(b[row][col]) + " ", end='') 

def findEmpty(b):

    for row in range(len(b)):
        for col in range(len(b[row])):
            if b[row][col] == 0:
                return (row,col)
    return None

def isValid(b, num, pos):
    '''
    b = board
    num = loop iteration 1 - 10
    pos = 0 location
    '''
    #Check row
    for col in range(len(b[0])):
        if b[pos[0]][col] == num and pos[1] != col:
            return False

    #Check column
    for row in range(len(b)):
        if b[row][pos[1]] == num and pos[0] != row:
            return False

    #Check box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range (box_x * 3, box_x * 3 + 3):
        for j in range (box_y * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(board):

    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0

    return False


printBoard(board)
print("--------------------------")
solve(board)
printBoard(board)
