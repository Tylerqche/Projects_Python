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

#------------------------------------------------------------#

def printBoard(b):

    for row in range (len(b)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        
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

#------------------------------------------------------------#

def validBoard(board):
    
    if validNumbers(board):
        #Check row
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                temp += [board[i][j]]
            if len(temp) != len(set(temp)):
                return False

        #Check horizontal
        for i in range(len(board[0])):
            temp = []
            for j in range(len(board)):
                temp += [board[j][i]]
            if len(temp) != len(set(temp)):
                return False

        #Check box
        for i in range(len(board)):
            count = 0
            temp = []
            for j in range(len(board[0])):
                x_square = j // 3
                y_square = j % 3

                x_place = (i // 3) * 3
                y_place = (i % 3) * 3
                
                pos_x = x_square + x_place
                pos_y = y_square+y_place

                temp += [board[pos_x][pos_y]]
            if len(temp) != len(set(temp)):
                return False

        return True
    else:
        print("Invalid Units!")

def validNumbers(board):
    allowed = {0,1,2,3,4,5,6,7,8,9}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not allowed.issuperset([board[i][j]]):
                return False
    return True

#------------------------------------------------------------#

def main():
    printBoard(board)
    print("---------------------")
    solve(board)
    if validBoard(board):
        printBoard(board)
    elif validBoard(board) == False:
        print("Error solving board!")
main()
