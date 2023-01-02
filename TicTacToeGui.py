from tkinter import *
from tkinter import messagebox

#-------------------------------------------------------------------------------------#
def displayBoard(board):
    '''
    Print's board'''
    for rows in range(3):
        print(board[rows])

def checkWinner(b):

    #Check row
    for row in range(len(board[0])):
        mark = board[row][0]
        if mark == "":
            continue
        match = 1
        for col in range(1,3):
            if mark == board[row][col]:
                match += 1
        if match == 3:
            return True

    #Check column
    for col in range(len(board)):
        mark = board[0][col]
        if mark == "":
            continue
        match = 1
        for row in range(1,3):
            if mark == board[row][col]:
                match += 1
        if match == 3:
            return True

    #Check diagonal
    diagonal_one = [board[i][i] for i in range(len(board))]
    diagonal_two = [board[i][len(board)-i-1] for i in range(len(board))]
    match = 0
    for i in range(len(diagonal_one)):
        mark = diagonal_one[0]
        if diagonal_one[i] == mark:
            if mark == "":
                continue
            match += 1
    if match == 3:
        return True
    else:
        match = 0

    match2 = 0
    for i in range(len(diagonal_two)):
        mark = diagonal_two[0]
        if diagonal_two[i] == mark:
            if mark == "":
                continue
            match2 += 1
    if match2 == 3:
        return True
        
    return False

def checkBoardFilled(board):
    '''
    Check's if the board is filled
    '''

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                return False
    return True

#-------------------------------------------------------------------------------------#

def main():

    if whoClick == False:
        mark = 'X'
    elif whoClick == True:
        mark = 'O'

    if checkWinner(board) == True:
        winner = messagebox.showinfo("Winner" , mark + " Won!")
        root.quit()
        return
    elif checkBoardFilled(board) == True:
        winner = messagebox.showinfo("Tie", "Both players tie!")
        root.quit()
        return

#-------------------------------------------------------------------------------------#

root = Tk()
root.title("Tictactoe GUI")
window = Canvas(root, bg = "gray")
#root.wm_attributes('-toolwindow', 'True')

whoClick = True
count = 0

'''
X moves first
whoClick = True is X
whoClick = False = O
'''
def onClick(row, col):

    global whoClick, count

    if button[row][col]["text"] == " " and whoClick == True:
        button[row][col].configure(
                            fg="green", bg="lightgray",
                            activebackground="lightgray",
                            activeforeground="green")
        button[row][col]["text"] = "X"
        board[row][col] = "X"
        #button[row][col].configure(state="disabled")
        whoClick = False
    elif button[row][col]["text"] == " " and whoClick == False:
        button[row][col].configure(
                            fg="red",bg="lightgray",
                            activebackground="lightgray",
                            activeforeground="red")
        button[row][col]["text"] = "O"
        board[row][col] = "O"
        #button[row][col].configure(state="disabled")
        whoClick = True
    else:
        click = messagebox.showinfo("Invalid", "Space filled!")

    main()
            
button = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
board = [
    ["","",""],
    ["","",""],
    ["","",""]
]

for i in range(3):
    for j in range(3):
        button[i][j] = Button(
                        root, text = " ", bd = 1,
                        font = ("Helvetica", 20), 
                        height = 3, width = 6, 
                        command = lambda r = i, c = j : onClick(r, c))
        button[i][j].grid(row = i, column = j)

root.mainloop()

#-------------------------------------------------------------------------------------#
