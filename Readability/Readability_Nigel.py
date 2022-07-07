from re import L


text =input("Input the text to be graded: ")

arr = text.split()

#L is average number of letters per 100 words.
L = 0 

W = 1
# S is average number of sentences per 100 words.
S = 0
for char in text:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <='Z'):
        L += 1
    elif (char < 'a' or char > 'z') and (char < 'A' or char > 'Z'):
        if char == '!' or char == '.' or char == '?':
            S += 1 
        elif char == " ":
            W += 1


Fin_L = L / W * 100
Fin_S = S / W * 100
index = 0.0588 * Fin_L - 0.296 * Fin_S - 15.8
finalGrade = round(index)
print("Number of letters: ", L)
print("Number of words: ", W)
print("Number of sentences: ", S)
if finalGrade < 1:
    print("Before Grade 1")
elif finalGrade > 16:
    print ("Grade 16+")
else:
    print("Grade: ", finalGrade)


