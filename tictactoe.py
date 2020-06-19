import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def print_board(lst):
    b = """ 
            A    B    C

      1     {} |  {}  | {}
          ----+-----+----
      2     {} |  {}  | {}
          ----+-----+----
      3     {} |  {}  | {}
        """
    print(b.format(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8]))

def ask_move(j):
    print_board(board)
    i = input("It is " + xoro + "'s chance. Enter your choice: ")
    i = i.capitalize()
    if (i == "A1"):
        board[0] = j
    if (i == "B1"):
        board[1] = j
    if (i == "C1"):
        board[2] = j
    if (i == "A2"):
        board[3] = j
    if (i == "B2"):
        board[4] = j
    if (i == "C2"):
        board[5] = j
    if (i == "A3"):
        board[6] = j
    if (i == "B3"):
        board[7] = j
    if (i == "C3"):
        board[8] = j

def switch(k):
    if (k == "X"):
        return("O")
    else:
        return("X")

print("Welcome to Tic-Tac-Toe!")
print("Your turn first.")
xoro = input("Do you want X or O: ").capitalize()

def checkgame(lst):
    if (lst[0] == lst[1] == lst[2] == xoro):
        return(xoro)
    elif (lst[3] == lst[4] == lst[5] == xoro):
        return(xoro)
    elif (lst[6] == lst[7] == lst[8] == xoro):
        return(xoro)
    elif (lst[0] == lst[3] == lst[6] == xoro):
        return(xoro)
    elif (lst[1] == lst[4] == lst[7] == xoro):
        return(xoro)
    elif (lst[2] == lst[5] == lst[8] == xoro):
        return(xoro)
    elif (lst[0] == lst[4] == lst[8] == xoro):
        return(xoro)
    elif (lst[6] == lst[4] == lst[2] == xoro):
        return(xoro)
    elif (" " in lst == False):
        return("tie")

def checkrow(a,b,c):
    o = 0
    if ((board[a] == board[b] == xoro) & (board[c] == " ")):
        return(c)
        o = 1
    elif ((board[b] == board[c] == xoro) & (board[a] == " ") & (o == 0)):
        return(a)
        o = 1
    elif ((board[a] == board[c] == xoro) & (board[b] == " ") & (o == 0)):
        return(b)
        o = 1
    elif ((board[a] == board[b] == switch(xoro)) & (board[c] == " ") & (o == 0)):
        return(c)
        o = 1
    elif ((board[b] == board[c] == switch(xoro)) & (board[a] == " ") & (o == 0)):
        return(a)
        o = 1
    elif ((board[a] == board[c] == switch(xoro)) & (board[b] == " ") & (o == 0)):
        return(b)

def nextmove():
    if (type(checkrow(0,1,2)) == int):
        board[checkrow(0,1,2)] = xoro
        return("done")
    elif (type(checkrow(3,4,5)) == int):
        board[checkrow(3,4,5)] = xoro
        return("done")
    elif (type(checkrow(6,7,8)) == int):
        board[checkrow(6,7,8)] = xoro
        return("done")
    elif (type(checkrow(0,3,6)) == int):
        board[checkrow(0,3,6)] = xoro
        return("done")
    elif (type(checkrow(1,4,7)) == int):
        board[checkrow(1,4,7)] = xoro
        return("done")
    elif (type(checkrow(2,5,8)) == int):
        board[checkrow(2,5,8)] = xoro
        return("done")
    elif (type(checkrow(0,4,8)) == int):
        board[checkrow(0,4,8)] = xoro
        return("done")
    elif (type(checkrow(2,4,6)) == int):
        board[checkrow(2,4,6)] = xoro
        return("done")

def rad():
    l = []
    for i in range(9):
        if (board[i] == " "):
            l.append(i)
    if(len(l) > 0):
        board[random.choice(l)] = xoro



while (True):
    ask_move(xoro)
    if (checkgame(board) == xoro):
        print_board(board)
        print(xoro, "has won!")
        break
    elif (checkgame(board) == "tie"):
        print("Tie!")
        break
    xoro = switch(xoro)
    k = nextmove()
    if (k != "done"):
        rad()

    if(checkgame(board) == xoro):
        print_board(board)
        print(xoro, "has won!")
        break
    elif(checkgame(board) == "tie"):
        print("Tie!")
        break
    else:
        xoro = switch(xoro)