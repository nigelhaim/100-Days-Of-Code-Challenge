'''
100 Days of Code -- Day 8
Readability -- CS50
Alyza Paige L. Ng
'''
#get text from user
text = input("Enter a text: ")
count_letter = count_sentence = 0
count_word = 1

for i in range(len(text)):
	#count the number of letters in a word
	if text[i].isalpha():
		count_letter += 1

	#count the number of words in a sentence
	if text[i].isspace():
		count_word += 1

	#count the number of sentences in a text
	if text[i] == '.' or text[i] == '?' or text[i] == '!':
		count_sentence += 1

#readability formula = (0.0588 * L) - (0.296 * S) - 15.8
grade = round((0.0588 * (count_letter / count_word) * 100) - (0.296 * (count_sentence / count_word) * 100) - 15.8)

print("Readability: ", end="")
if grade < 1:
	print("Before Grade 1")
elif grade > 16:
	print("Grade 16+")
else:
	print(f"Grade {grade}")