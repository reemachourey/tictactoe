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
  print (board[0] + " | " + board[1] +" | "+ board[2])
  print (board[3] + " | " + board[4] +" | "+ board[5])
  print (board[6] + " | " + board[7] +" | "+ board[8])
  
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
    print(winner + "won.")
  elif winner =="None":
    print("Tie.")


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  #checkcolumns
  #check diagonals
  return

def check_rows():
  return

def check_col():
  return

def check_diagonal():
  return

def check_if_tie():
  return

#flip the player
def flip_player():
  global current_player
  if(current_player=="X"):
    current_player="O"
  else:
    current_player="X"


#handle a single turn
def handle_turn(player):
  pos = input("Enter your position from 1 to 9 : ")
  pos=int(pos)-1

  board[pos]=player
  
  display_board()


#start the game
play_game()