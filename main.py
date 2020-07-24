#board
#Disply board
#play game
#check win
  #check rows
  #checkcolumns
  # diagonals

#checktie
#flipplayer

#--global variables ----

#game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if game is still game_still_going
game_still_going=True

#who won
winner=None
#if tie then winner is none only

#whose turn isinstance
current_player="X"

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")
  
#----------------------function------------------------------  
#play game of tic tac toe
def play_game():
  
  #Display initial board
  display_board() 
  
  while game_still_going:

    handle_turn(current_player)

    #chcek if game has ended
    check_if_game_over()
      
      # Flip to the other player
    flip_player()

  #game has ended
  if winner=="X" or winner=="O":
    print(winner + " won.")
  elif winner == None :
    print("Tie.")


def check_if_game_over():
  check_for_winner()
  check_if_tie()
    

def check_for_winner():
  #set up global variable
  global winner
  #checkcolumns
  column_winner=check_columns()
  
  #check rows
  row_winner=check_rows()
  
  #check diagonals
  diagonal_winner=check_diagonal()

  if column_winner:
    print("column")
    winner=column_winner
  elif row_winner:
    print("row")
    winner=row_winner
  elif diagonal_winner:
    print("diagonal")
    winner=diagonal_winner
  else:
    winner=None 

def check_rows():
  #global variable
  global game_still_going
  #check if any of the rows have all the same values
  r1=board[0] == board[1] == board[2] != "-"
  r2=board[3] == board[4] == board[5] != "-"
  r3=board[6] == board[7] == board[8] != "-"
  if r1 or r2 or r3:
    game_still_going=False
    
  if r1: 
    board[0]
  elif r2:
    board[3]
  elif r3:
    board[6]
  else:
    return None

def check_columns():
  #global variable
  global game_still_going
  #check if any of the columns have all the sma evalues
  c1=board[0] == board[3] == board[6] != "-"
  c2=board[1] == board[4] == board[7] != "-"
  c3=board[2] == board[5] == board[8] != "-"
  if c1 or c2 or c3:
    game_still_going=False
    
  if c1: 
    board[0]
  elif c2:
    board[1]
  elif c3:
    board[2]
  else:
    return None

def check_diagonal():
  #global variable
  global game_still_going
  dia1=board[0] == board[4] ==board[8] !="-"
  dia2=board[2] == board[4] ==board[6] !="-"
  if dia1 or dia2 :
    game_still_going=False
  if dia1:
    return board[0]
  elif dia2:
    return board[2]
  else:
    return None

def check_if_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False

#flip the player
def flip_player():
  global game_still_going
  global current_player
  if game_still_going:
    if(current_player=="X"):
      current_player="O"
    else:
      current_player="X"
  return

#handle a single turn
def handle_turn(player):
  print(player +"'s turn")
  pos = input("Enter your position from 1 to 9 : ")

  valid=False
  while not valid:

    while pos not in ["1","2","3","4","5","6","7","8","9"]:
      print(player +"'s turn")
      pos = input("Invalid input, enter your position from 1 to 9 : ")
  
    pos = int(pos)-1

    if(board[pos]=="-"):
      valid=True
    else:
      print("You cant go there, position already occupied")
  
  board[pos]=player
  
  display_board()

#start the game
play_game()