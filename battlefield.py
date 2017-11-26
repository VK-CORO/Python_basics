from random import randint       #importing the "randint" to get the random integer 

board = []    #empty board                  

for x in range(0, 5):
  board.append(["O"] * 5)  #adding '0' values to the board for five times

def print_board(board):
  for row in board:
    print " ".join(row)   #arranging 0's to look like '0 0 0 0 0'. Now it looks like matrix

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)    

def random_col(board):
  return randint(0, len(board[0]) - 1)   #Actually random_col & random_row are the answer for this battleship game.It'll give random integers. 
 
ship_row = random_row(board)
ship_col = random_col(board)    
print ship_row
print ship_col     #Here i just used print ship_row & ship_col to show you what is happening. if you don't want you can remove this.because this actually an answer 

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1     #It will print the number of turns

  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))     #here we guess our row and column to find the battleship

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"     
    break              #It returns above statement when you guess the correct column and row and will break the loop running.                             
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."    #It will return this statement if you type row and column values from out of range

    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )    #This will warn if you type the same values again and replace '0' with 'X' after we give our input values

    else:
      print "You missed my battleship!"    #Finally if you can't find the battleship
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)   