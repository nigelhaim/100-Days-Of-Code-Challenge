import random
moves = ['R', 'P', 'S']

pc_num = random.randint(0, 2)

pc_move= moves[pc_num]

print("R - Rock \nP - Paper \nS - Scissors")

move = ''
while move != 'R' and move != 'P' and move != 'S': 
    move = input("Input your move (R|P|S):").upper()

if (pc_move == 'R' and move == 'P') or (pc_move == 'P' and move == 'S') or (pc_move == 'S' and move == 'R'):
    print("You Win!")
elif pc_move == move:
    print("Its a tie!")
else:
    print("You Loose!")

print("Player move: ", move)
print("Computer move: ", pc_move)