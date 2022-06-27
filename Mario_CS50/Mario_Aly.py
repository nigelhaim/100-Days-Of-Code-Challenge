#100 Days of Code -- Day 3
#Mario -- CS50
#Alyza Paige L. Ng

rows = int(input('Enter the number of rows: '))
for row in range(1, rows + 1):
    print(' ' * (rows - row) + '#' * row + '  ' + '#' * row)