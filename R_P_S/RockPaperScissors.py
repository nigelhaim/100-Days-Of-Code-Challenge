'''
100 Days of Code -- Day 9
Rock Paper Scissors
Alyza Paige L. Ng
'''
import random

while True:
	def play(player_choice, computer_choice):
		if computer_choice == loses_to[player_choice]:
			return "You win!"
		elif player_choice == loses_to[computer_choice]:
			return "You lose!"
		return "It's a tie!"

	choices = ['rock', 'paper', 'scissors']
	player_choice = None
	computer_choice = random.choice(choices)
	print(computer_choice)

	while player_choice not in choices:
		player_choice = input("Rock, paper, or scissors?: ").lower()

	loses_to = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
	print(f"You chose \'{player_choice}\', and the computer chose \'{computer_choice}\'...\n{play(player_choice, computer_choice)}")

	again = input("Do you wish to play again? (yes/no): ").lower()
	print()
	if again != 'yes':
		break
print("Thank you for playing! Bye!")