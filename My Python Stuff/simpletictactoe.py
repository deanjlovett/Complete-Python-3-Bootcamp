from IPython.display import clear_output

is_game_on = True
board = []
is_x_move = True
legal_pos = []
quit_pos = ["Q","QUIT","EXIT","E"]


def init_legal_pos(legal_pos):
    letters = ['A','B','C']
    for c in letters:
        for i in range(1,4):
            legal_pos.append(c+str(i))
    # legal_pos.append("X")
    # legal_pos.append("EXIT")
    legal_pos.append("Q")
    legal_pos.append("QUIT")
    print(legal_pos)


def init_board(bd):
    for i in range(0,10):
        bd.append('#')

def clear_board(bd):
    for i in range(0,10):
        bd[i]=' '


def clear_screen():
    pass

def display_whose_move():
    if is_x_move:
        print("It is X's move:")
    else:
        print("It is O's move:")

def display_board(bd,display_whose=True):
    print()
    if display_whose:
        display_whose_move()
    print()
    print( "  1|2|3")
    print(f"A {bd[0]}|{bd[1]}|{bd[2]}")
    print( "  -+-+-")
    print(f"B {bd[3]}|{bd[4]}|{bd[5]}")
    print( "  -+-+-")
    print(f"C {bd[6]}|{bd[7]}|{bd[8]}")
    print()
    if display_whose:
        display_whose_move()
    print()

def pos_choice():
        
    choice = 'wrong'
    while choice not in legal_pos:
        
        choice = input("Pick a position for mark [A1,A2,A3,B1,B2...]: ").upper()
        print()
        print("position selected:",choice)
        
        if choice not in legal_pos:
            print("Sorry, but you did not choose a valid position [A1,A2,A3,B1,B2...]")
            print()
            display_whose_move()
        print()
        
    return choice

def apply_choice(board,pos):
    row = ord(pos[0])-ord('A')
    col = int(pos[1])-1
    if board[row*3+col] != ' ':
        print("Sorry, Dave... I can't do that. There is a piece already there.")
        return board, False
    elif is_x_move:
        board[row*3+col] = 'X'
    else:
        board[row*3+col] = 'O'
    return board, True

def check_for_win(board):
    if  ((board[0] == board[3] == board[6] ) and (board[0]!=' ')) or \
        ((board[1] == board[4] == board[7] ) and (board[1]!=' ')) or \
        ((board[2] == board[5] == board[8] ) and (board[2]!=' ')) or \
        ((board[0] == board[1] == board[2] ) and (board[0]!=' ')) or \
        ((board[3] == board[4] == board[5] ) and (board[3]!=' ')) or \
        ((board[6] == board[7] == board[8] ) and (board[6]!=' ')) or \
        ((board[0] == board[4] == board[8] ) and (board[0]!=' ')) or \
        ((board[2] == board[4] == board[6] ) and (board[2]!=' ')):
        display_board(board,False)
        print()
        if is_x_move:
            print("X wins !!")
        else:
            print("O wins !!")
        return True
    return False
    

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','y','N','n']:
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','y','N','n']:
            #clear_output()
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice == "Y" or choice=="y":
        return True
    else:
        return False    

init_board(board)
init_legal_pos(legal_pos )
clear_board(board)

while is_game_on:
    clear_screen()
    display_board(board)
    pos = pos_choice()
    if pos in quit_pos:
        print("Quitting game.")
        break
    board,ok = apply_choice(board,pos)
    if ok:
        if check_for_win(board):
            break
        if is_x_move:
            is_x_move = False
        else:
            is_x_move = True
    clear_screen()
    #display_board(board)
    # is_game_on = gameon_choice()
