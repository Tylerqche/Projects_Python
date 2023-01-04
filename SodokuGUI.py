import tkinter as tk
import time as time

def onClick():
    solveButton.configure(text="Solving.",
                          bg="lightgray",
                          activebackground="lightgray",
                          font=("Helvetica", 12))
    root.update()
    time.sleep(0.5)
    solveButton.configure(text="Solving..")
    root.update()
    time.sleep(0.5)
    solveButton.configure(text="Solving...")
    root.update()
    time.sleep(0.5)
    
    solve(board)

    if validBoard(board):
        solveButton.configure(text="Solved!",
                          bg="lightgray",
                          activebackground="lightgray",
                          font=("Helvetica", 12))
        root.update()
        time.sleep(3)
        root.quit()
                          
    elif validBoard(board) == False:
        solveButton.configure(text="Error!",
                          bg="lightgray",
                          activebackground="lightgray",
                          font=("Helvetica", 12))
        root.update()
        time.sleep(3)
        root.quit()
    

#------------------------------------------------#

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
        unsolvedText = tk.StringVar()
        buttonCell[row][col].configure(textvariable=unsolvedText,
                                       bg="lightgray")
        unsolvedText.set(i)
        root.update()
        time.sleep(0.05)
        if isValid(board, i, (row, col)):
            time.sleep(0.005)
            board[row][col] = i
            solvedText = tk.StringVar()
            buttonCell[row][col].configure(textvariable=solvedText,
                                           bg="white")
            solvedText.set(i)
            root.update()
            
            if solve(board):
                return True
            board[row][col] = 0
            solvedText = tk.StringVar()
            buttonCell[row][col].configure(textvariable=solvedText,
                                           bg="lightgray")
            solvedText.set(i)
            root.update()
            time.sleep(0.005)

    return False

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
        return False

def validNumbers(board):
    allowed = {0,1,2,3,4,5,6,7,8,9}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not allowed.issuperset([board[i][j]]):
                return False
    return True
    
#------------------------------------------------#

root = tk.Tk()
root.title("Sodoku GUI")

blocks = [
    ["","",""],
    ["","",""],
    ["","",""]
]

buttonCell = [
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','','']
]

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


window = tk.LabelFrame(root, text="Sodoku Solver",
                       font=("Helvetica", 10),
                       padx=5, pady=5
                       )

for i in range(len(blocks)):
    for j in range(len(blocks[0])):
        blocks[i][j] = tk.Frame(window, bd=2, highlightbackground='lightgray',
                                highlightthickness=1,
                                padx=5, pady=5
                                )
        blocks[i][j].grid(row=i, column=j)
window.pack(padx=5,pady=5)

for i in range(len(buttonCell)):
    for j in range(len(buttonCell[0])):
        cell = tk.Frame(blocks[i // 3][j // 3])
        cell.grid(row=(i % 3), column=(j % 3))
        cell.rowconfigure(0, minsize=50, weight=1)
        cell.columnconfigure(0, minsize=50, weight=1)
        buttonText = tk.StringVar()
        buttonCell[i][j] = tk.Button(cell, relief='ridge', bg='white',
                                     textvariable=buttonText,
                                     font=("Helvetica", 15))
        buttonCell[i][j].grid(sticky='nsew')
        buttonText.set(board[i][j])

solveButton = tk.Button(root, text="Solve Board", font=("Helvetica", 12), 
                        heigh = 2, width = 10,
                        command = onClick)
solveButton.pack(padx=5,pady=(0,5))

root.mainloop()

#------------------------------------------------#