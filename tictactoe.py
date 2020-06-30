import random

print("Welcome to Tic-Tac-Toe.")
xoro = input("Do you want X or O: ").capitalize()
print("Your turn first.")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():      # function to print the board
    b = """
            A    B    C

      1     {} |  {}  | {}
          ----+-----+----
      2     {} |  {}  | {}
          ----+-----+----
      3     {} |  {}  | {}
        """
    print(b.format(board[0], board[1], board[2], board[3],
          board[4], board[5], board[6], board[7], board[8]))

# function which checks status of board and returns:
# "X" if X has won
# "O" if O has won
# "tie" if game is a tie
# 0 if game can continue

def check_board():
    if ((board[0] == board[1] == board[2] == "X") or (board[0] == board[1] == board[2] == "O")):
        return(board[0])
    elif ((board[3] == board[4] == board[5] == "X") or (board[3] == board[4] == board[5] == "O")):
        return(board[3])
    elif ((board[6] == board[7] == board[8] == "X") or (board[6] == board[7] == board[8] == "O")):
        return(board[6])
    elif ((board[0] == board[3] == board[6] == "X") or (board[0] == board[3] == board[6] == "O")):
        return(board[0])
    elif ((board[1] == board[4] == board[7] == "X") or (board[1] == board[4] == board[7] == "O")):
        return(board[1])
    elif ((board[2] == board[5] == board[8] == "X") or (board[2] == board[5] == board[8] == "O")):
        return(board[2])
    elif ((board[0] == board[4] == board[8] == "X") or (board[0] == board[4] == board[8] == "O")):
        return(board[0])
    elif ((board[6] == board[4] == board[2] == "X") or (board[6] == board[4] == board[2] == "O")):
        return(board[6])
    elif (" " not in board):
        return(0)


def switch():   # function to return opposite character of whatever the player has chosen
    if (xoro == "X"):
        return("O")
    if (xoro == "O"):
        return ("X")


def check_three(a, b, c, d):    # function which returns int if the given triplet has just one empty square
    l = [board[a], board[b], board[c]]
    k = [a, b, c]
    if ((l.count(d) == 2) & (l.count(" ") == 1)):
        return (k[l.index(" ")])


def free_squares(k):     # function which returns list of indices of free squares
    lst = []
    for i in range(len(k)):
        if ((k[i] == " ") & (i not in left)):
            lst.append(i)
    return (lst)

def free_squares_temp(k):     # function which returns list of indices of free squares
    lst = []
    for i in range(len(k)):
        if (k[i] == " "):
            lst.append(i)
    return (lst)

def check_three_temp(a, b, c, d, e):    # function which returns int if the given triplet has just one empty square
    l = [e[a], e[b], e[c]]
    k = [a, b, c]
    if ((l.count(d) == 2) & (l.count(" ") == 1)):
        return (k[l.index(" ")])

def avoid_trip2(p):
    board_temp = p.copy()
    for i in free_squares_temp(board_temp):
        board_temp[i] = xoro
        j = 0
        if (type(check_three_temp(0, 1, 2, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(3, 4, 5, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(6, 7, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(0, 3, 6, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(1, 4, 7, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(2, 5, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(0, 4, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(2, 4, 6, xoro, board_temp)) == int):
            j+=1
        if ((j > 1) & (i not in left)):
            return(i)
        else:
            board_temp = p.copy()

def avoid_trip3(p):
    board_temp = p.copy()
    for i in free_squares_temp(board_temp):
        board_temp[i] = xoro
        j = 0
        if (type(check_three_temp(0, 1, 2, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(3, 4, 5, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(6, 7, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(0, 3, 6, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(1, 4, 7, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(2, 5, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(0, 4, 8, xoro, board_temp)) == int):
            j+=1
        if (type(check_three_temp(2, 4, 6, xoro, board_temp)) == int):
            j+=1
        if (j > 1):
            return(i)
        else:
            board_temp = p.copy()

def avoid_trip():
    for i in range(6):
        if(type(avoid_trip2(board)) == int):
            board_temp2 = board.copy()
            board_temp2[avoid_trip2(board_temp2)] = switch()
            if((type(avoid_trip3(board_temp2)) == int) == False):
                return(avoid_trip2(board))
            else:
                left.append(avoid_trip2(board))


def special_case():
    if ((board[4] == xoro) & (([board[0], board[1], board[2], board[3], board[5], board[6], board[7], board[8]]).count(xoro) == 1)):
        if (board[0] == xoro):
            return(2)
        if (board[2] == xoro):
            return(8)
        if (board[6] == xoro):
            return(0)
        if (board[8] == xoro):
            return(6)

# function which return the recommended move
# this is where all the logic is built in
# first priority is to complete triad and win
# second priority is to save completion of enemy triad
# third choice are special cases
# fourth choice is to avoid double enemy triads
# fifth choice is random move

def next_move():
    # logic to complete triplet first
    global left
    left = []
    if (type(check_three(0, 1, 2, switch())) == int):
        return (check_three(0, 1, 2, switch()))
    elif (type(check_three(3, 4, 5, switch())) == int):
        return (check_three(3, 4, 5, switch()))
    elif (type(check_three(6, 7, 8, switch())) == int):
        return (check_three(6, 7, 8, switch()))
    elif (type(check_three(0, 3, 6, switch())) == int):
        return (check_three(0, 3, 6, switch()))
    elif (type(check_three(1, 4, 7, switch())) == int):
        return (check_three(1, 4, 7, switch()))
    elif (type(check_three(2, 5, 8, switch())) == int):
        return (check_three(2, 5, 8, switch()))
    elif (type(check_three(0, 4, 8, switch())) == int):
        return (check_three(0, 4, 8, switch()))
    elif (type(check_three(2, 4, 6, switch())) == int):
        return (check_three(2, 4, 6, switch()))
    # logic to avoid enemy triplet second
    elif (type(check_three(0, 1, 2, xoro)) == int):
        return (check_three(0, 1, 2, xoro))
    elif (type(check_three(3, 4, 5, xoro)) == int):
        return (check_three(3, 4, 5, xoro))
    elif (type(check_three(6, 7, 8, xoro)) == int):
        return (check_three(6, 7, 8, xoro))
    elif (type(check_three(0, 3, 6, xoro)) == int):
        return (check_three(0, 3, 6, xoro))
    elif (type(check_three(1, 4, 7, xoro)) == int):
        return (check_three(1, 4, 7, xoro))
    elif (type(check_three(2, 5, 8, xoro)) == int):
        return (check_three(2, 5, 8, xoro))
    elif (type(check_three(0, 4, 8, xoro)) == int):
        return (check_three(0, 4, 8, xoro))
    elif (type(check_three(2, 4, 6, xoro)) == int):
        return (check_three(2, 4, 6, xoro))
    # logic for special case of first corner move
    elif (([board[0], board[2], board[6], board[8]].count(xoro) == 1) & ([board[1], board[3], board[4], board[5], board[7]].count(" ") == 5)):
        return (4)
    # logic for special case of first centere move
    elif (board == [" ", " ", " ", " ", xoro, " ", " ", " ", " "]):
        return(random.choice([0, 2, 6, 8]))
    elif(type(special_case()) == int):
        return(special_case())
    # logic for special case of first edge move
    elif (([board[1], board[3], board[5], board[7]].count(xoro) == 1) & ([board[0], board[2], board[4], board[6], board[8]].count(" ") == 5)):
        return(4)
    # logic for avoiding double triplets of enemy 2 moves ahead
    elif (type(avoid_trip()) == int):
        return(avoid_trip())
    # Space for adding logic

    # logic for random move
    else:
        return(random.choice(free_squares(board)))


def convert(a):     # function to conver user input to the board list index
    if(a == "A1"):
        return(0)
    if(a == "B1"):
        return(1)
    if(a == "C1"):
        return(2)
    if(a == "A2"):
        return(3)
    if(a == "B2"):
        return(4)
    if(a == "C2"):
        return(5)
    if(a == "A3"):
        return(6)
    if(a == "B3"):
        return(7)
    if(a == "C3"):
        return(8)


# main loop starts
while (True):
    print_board()
    board[convert(input("Enter your choice: ").capitalize())] = xoro
    if (check_board() == 0):
        print_board()
        print("It's a tie! :|")
        break
    elif (check_board() == xoro):
        print_board()
        print("Congratulations! You won :)")
        break

    board[next_move()] = switch()
    if (check_board() == switch()):
        print_board()
        print("You lost :(")
        break
