'''
100 Days of Code -- Day 5
Day 5 -- Tic-Tac-Toe Game
Alyza Paige L. Ng
'''
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#prints the board
def print_board(board):
	print(" " + board[0] + " | " + board[1] + " | " + board[2] + "\n---|---|---")
	print(" " + board[3] + " | " + board[4] + " | " + board[5] + "\n---|---|---")
	print(" " + board[6] + " | " + board[7] + " | " + board[8])

#swaps the player after every turn
def swap_player(symbol):
    return 'X' if symbol == 'O' else 'O'

def check_row(board):
	#top row
	if board[0] == board[1] == board[2] != ' ':
		return True
	#middle row
	elif board[3] == board[4] == board[5] != ' ':
		return True
	#bottom row
	elif board[6] == board[7] == board[8] != ' ':
		return True
	return False

def check_column(board):
	#left column
	if board[0] == board[3] == board [6] != ' ':
		return True
	#middle column
	elif board[1] == board[4] == board[7] != ' ':
		return True
	#right column
	elif board[2] == board[5] == board[8] != ' ':
		return True
	return False

def check_diagonals(board):
	#downward diagonal
	if board[0] == board[4] == board[8] != ' ':
		return True
	#upward diagonal
	elif board[2] == board[4] == board[6] != ' ':
		return True
	return False

def declare_winner(symbol, board):
	print_board(board)
	print(f"\nGAME OVER\nPlayer {symbol} wins!")

def start_game():
	board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	print("Welcome to Tic-Tac-Toe!")
	symbol = 'O'
	count = 0
	
	for i in range(9):
		print_board(board)
		print(f"It's your turn, Player {symbol}!")
		try:
			move = int(input("Enter your move (Select a number from 1-9): "))
			if move < 1 and move > 9:
				raise Exception(e)
		except:
			print("Sorry, you are only allowed to enter a number from 1 to 9.")
			continue

		#slot is taken
		if board[move-1] != ' ':
			move = int(input("That spot is already taken!\nEnter another spot: "))
		board[move-1] = symbol
		count += 1

		if check_row(board):
			declare_winner(symbol, board)
			break
		elif check_column(board):
			declare_winner(symbol, board)
			break
		elif check_diagonals(board):
			declare_winner(symbol, board)
			break
		
		symbol = swap_player(symbol)
		
	#both players filled all the slots but did not win
	if count == 9:
		print_board(board)
		print("\nGAME OVER\nIt's a tie!")

	restart = input("\nDo you want to play again? (y/n): ").lower()
	if restart == 'y':
		print()
		start_game()
	elif restart == 'n':
		print("\nThank you for playing!")
	else:
		print("\nInvalid input.\nExiting program...")

start_game()