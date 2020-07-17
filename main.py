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
  print("")
  print (board[0] + " | " + board[1] +" | "+ board[2])
  print (board[3] + " | " + board[4] +" | "+ board[5])
  print (board[6] + " | " + board[7] +" | "+ board[8])
  print("")
  
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
  elif winner =="None":
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
    winner=column_winner
  elif row_winner:
    winner=row_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    winner=None 

def check_rows():
  #global variable
  global game_still_going
  #check if any of the rows have all the sma evalues
  for i in range(0,3):
    if(board[i] == board[i+1] == board[i+2] != "-"):
        game_still_going=False
        return board[i]
  return None

def check_columns():
  #global variable
  global game_still_going
  #check if any of the rows have all the sma evalues
  for i in range(0,3):
    if(board[i] == board[i+3] == board[i+6] != "-"):
        game_still_going=False
        return board[i]
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
  return winner==None

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