def beginGame():
    '''
    Begin's game, creates selection prompt
    Checks for invalid mark selection
    ''' 

    check = 0
    while check == 0:
        print("Player 1 please choose X or O")
        mark_one = str(input())
        if mark_one == 'X' or mark_one == 'O':
            print("Player 1's mark is: " + mark_one)
            check += 1
        else:
            print("Invalid mark selected. Try again.")
            check = 0
    
    if mark_one == 'X':
        mark_two = 'O'
        print("Player 2's mark is: " + mark_two)
    else: 
        mark_two = 'X'
        print("Player 2's mark is: " + mark_two)

    return [str(mark_one), str(mark_two)]

def isValid(row, col, board):
    '''
    Method to check if an inputted location is valid
    Check's user input
    Check's if spot is empty
    '''

    if not (row >= 0 and row < 3 and col >= 0 and col < 3):
        return False

    return board[row][col] == ' '

def createBoard():
    '''
    Create's board
    '''

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    return board

def displayBoard(board):
    '''
    Display's board
    '''
    print("   0   1   2 ")
    for i in range(len(board)):
        if i % 1 == 0 and i != 0:
            print("  - - - - - - ")
        
        for j in range(len(board[i])):
            if j % 1 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 0:
                print(str(i)+ "  " + str(board[i][j]), end="")
            elif j == 2:
                print(board[i][j])
            else:
                print(str(board[i][j]), end="")

def checkWinner(board):
    '''
    Check's for all win conditions
    '''

    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board) == True:
        return True
    else:
        return False

def checkVertical(board):
    '''
    Check's for vertical win
    '''

    for col in range(3):
        mark = board[0][col]
        if mark == " ":
            continue
        
        matches = 1
        for row in range(1,3):
            if mark == board[row][col]:
                matches += 1
        
        if matches == 3:
            return True
    return False

def checkHorizontal(board):
    '''
    Check's for horizontal win
    '''

    for row in range(3):
        mark = board[row][0]
        if mark == " ":
            continue
        
        matches = 1
        for col in range(1,3):
            if mark == board[row][col]:
                matches += 1
        
        if matches == 3:
            return True
    return False

def diagonalOne(board, row, col, increment):
    '''
    Check's left diagonal axis
    '''

    mark = board[row][col]
    if mark == " ":
        return False
  
    matches = 1
    for _ in range(2):
        row += increment
        col += increment
        if mark == board[row][col]:
            matches += 1
  
    return matches == 3

def diagonalTwo(board):
    '''
    Check's right diagonal axis
    '''
    mark = board[0][2]
    if mark == " ":
        return False
    matches = 1
    if mark == board[1][1]:
        matches +=1
    else:
        return False
    if mark == board[2][0]:
        matches +=1
    else:
        return False
    return matches == 3
    
def checkDiagonal(board):
    '''
    Check's for win condition on all diagonal axis
    '''

    return diagonalOne(board, 0, 0, 1) or diagonalTwo(board)

def checkBoardFilled(board):
    '''
    Check's if the board is filled
    '''

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

def playerMove(board, mark):
    '''
    Create's player moves prompt
    Check's if inputs are valid
    Check's if space is taken
    Re-does prompt if check's are invalid
    Display's updated board
    '''

    allowed = set("012")
    check = 0

    while check == 0:
        inputRow = input("Player " + mark + " please enter your row (0-2): ")
        inputCol = input("Player " + mark + " please enter your column (0-2): ")

        if allowed.issuperset(inputCol) and allowed.issuperset(inputRow) and inputRow != "" and inputCol != "":
            if isValid(int(inputRow),int(inputCol),board) == True:
                check += 1
                board[int(inputRow)][int(inputCol)] = mark
            elif isValid(int(inputRow),int(inputCol),board) == False:
                print("Invalid space eneterd!")
        else:
            print("Invalid input entered!")
    
    displayBoard(board)

def mainGame():
    '''
    Main game control prompt
    Gives prompt if player wins
    Gives prompt if players tie
    End's game
    '''

    board = createBoard()
    
    marks = beginGame()
    p1_mark = marks[0]
    p2_mark = marks[1]

    displayBoard(board)

    while True:
        for mark in [p1_mark, p2_mark]:
            playerMove(board, mark)
            
            if checkWinner(board) == True:
                print("Player " + mark + " wins!")
                return
            elif checkBoardFilled(board) == True:
                print("Both players tie!")
                return

mainGame()
