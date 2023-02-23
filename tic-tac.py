players = []
players_names = []
board = ['','','','','','','','','']
def pick_digit():
    booly = False
    player1 = 'wrong'
    player1_name = ''
    player2 = ''
    player2_name = ''
    while player1_name in ['']:
        player1_name = input('Please enter your name: ')
        players_names.append(player1_name)
        
    while player1 not in ['X','O']:
        player1 = input('Pick your mark (X or O): ')
        
    if player1 =='X':
        player2 = 'O'
        player2_name = input('Player 2 please enter your name: ')
        players.append(player1)
        players.append(player2)
        players_names.append(player2_name)
        
    elif player1 == 'O':
        player2 = 'X'
        player2_name = input('Player 2 please enter your name: ')
        players.append(player1)
        players.append(player2)
        players_names.append(player2_name)
        
    ready = input('Are u ready? (Y or N): ')
    
    while ready not in ['Y','N','y','n']:
        ready = input("I don't understand, type Y(yes) or N(no): ") 
        
    if ready.upper() == 'Y':
        booly = True
        
    while ready.upper() == 'N':
        ready = input('Type Y when u will be ready: ')
        if ready == 'Y':
            booly = True
    return booly

def pick_row():
    row = 'wrong'
    while row not in ['1','2','3']:
        row = input('Pick a row in which u want to put your mark(1,2,3 from up to down): ')
    return int(row)
        
def choose_position(actual_player,board,row1,pozycja1):
        if row1 == 1:
            if rzad1[pozycja1-1] == '':
                rzad1[pozycja1-1] = actual_player
            else:
                while rzad1[pozycja1-1] != '':
                    print('This place is already taken, choose another one')
                    pozycja1 = int(input('Pick a position in which u want to put your mark(1,2,3 form up to down): '))
                else:
                    rzad1[pozycja1-1] = actual_player
                    
        elif row1 == 2:
            if rzad2[pozycja1-1] == '':
                rzad2[pozycja1-1] = actual_player
            else:
                while rzad2[pozycja1-1] != '':
                    print('This place is already taken, choose another one')
                    pozycja1 = int(input('Pick a position in which u want to put your mark(1,2,3 form up to down): '))
                else:
                    rzad2[pozycja1-1] = actual_player
                    
        elif row1 == 3:
            if rzad3[pozycja1-1] == '':
                rzad3[pozycja1-1] = actual_player
            else:
                while rzad3[pozycja1-1] != '':
                    print('This place is already taken, choose another one')
                    pozycja1 = int(input('Pick a position in which u want to put your mark(1,2,3 form up to down): '))
                else:
                    rzad3[pozycja1-1] = actual_player
                    
    
def position():
    place = input('Now choose a position in row(1,2,3 from left to right): ')
    while place not in['1','2','3']:
        place = input('Pick a right number: ')
    return int(place)
   
from IPython.display import clear_output
rzad1 = [board[0],board[1],board[2]]
rzad2 = [board[3],board[4],board[5]]
rzad3 = [board[6],board[7],board[8]]

def display_game(board):
    print('Thats a current state of the game')
    print(rzad1)
    print('------------')
    print(rzad2)
    print("------------")
    print(rzad3)

def check_win(actual_player):
    if (rzad1[0] == 'X' and rzad1[1]== 'X' and rzad1[2] == 'X') or (rzad2[0] == 'X' and rzad2[1]== 'X' and rzad2[2] == 'X') or (rzad3[0] == 'X' and rzad3[1]== 'X' and rzad3[2] == 'X') or (rzad1[0] == 'X' and rzad2[0]== 'X' and rzad3[0] == 'X') or (rzad1[1] == 'X' and rzad2[1]== 'X' and rzad3[1] == 'X') or (rzad1[2] == 'X' and rzad2[2]== 'X' and rzad3[2] == 'X') or (rzad1[0] == 'X' and rzad2[1] == 'X' and rzad3[2] == 'X') or (rzad1[2]=='X' and rzad2[1]=="X" and rzad3[0]=='X') or (rzad1[0] == 'O' and rzad1[1]== 'O' and rzad1[2] == 'O') or (rzad2[0] == 'O' and rzad2[1]== 'O' and rzad2[2] == 'O') or (rzad3[0] == 'O' and rzad3[1]== 'O' and rzad3[2] == 'O') or (rzad1[0] == 'O' and rzad2[0]== 'O' and rzad3[0] == 'O') or (rzad1[1] == 'O' and rzad2[1]== 'O' and rzad3[1] == 'O') or (rzad1[2] == 'O' and rzad2[2]== 'O' and rzad3[2] == 'O') or (rzad1[0] == 'O' and rzad2[1] == 'O' and rzad3[2] == 'O') or (rzad1[2]=='O' and rzad2[1]=="O" and rzad3[0]=='O'):
        won = True
        if actual_player ==players[0]:
            print('{} won'.format(players_names[0]))
        else:
            print('{} won'.format(players_names[1]))
        return won


    
        
def game():
    
    hook = 0
    check = 1
    wePlaying = pick_digit()
    while wePlaying == True:
        if check > 9:
            print('Nobody won')
            break
        tablica = display_game(board)
        row = pick_row()
        pozycja = position()
        if hook%2 ==0:
            actual_player = players[0]
            
        else:
            actual_player = players[1]
        print(actual_player)
        choose_position(actual_player,tablica,row,pozycja)
        hook += 1
        check = check + 1
        won = check_win(actual_player)


        if won == True:
            odp = input('Do you wanna play once more? (Y OR N)')
            if odp in['Y']:
                game()
            else:
                break

game()      