POINTS = [1, 3, 3, 2, 1,
        4, 2, 4, 1, 8,
        5, 1, 3, 1, 1,
        3, 10, 1, 1, 1,
        1, 4, 4, 8, 4, 10]

def compute_Score(Str):
    score = 0
    for c in Str:
        score += POINTS[ord(c) - 65]
    return score

player1 = (input("Player 1: ").upper().strip())
player2 = (input("Player 2: ").upper().strip())

player1_Score = compute_Score(player1)
player2_Score = compute_Score(player2)
print()
if player1_Score > player2_Score:
    print("Player 1 wins!")
elif player2_Score > player1_Score:
    print("Player 2 wins!")
else:
    print("It is a tie!")

