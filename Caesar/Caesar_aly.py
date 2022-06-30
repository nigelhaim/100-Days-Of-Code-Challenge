'''
100 Days of Code -- Day 6
Caesar Cipher -- CS50
Alyza Paige L. Ng
'''

# encryption
def encrypt(text, key):
	result = ''
	for character in range(len(text)):
		char = text[character]
		if char.isupper():
			result += chr((ord(char) + key - ord('A')) % 26 + ord('A'))
		elif char.islower():
			result += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
		else:
			result += char
	return result

# decryption
def decrypt(text, key):
	result = ''
	for character in range(len(text)):
		char = text[character]
		if char.isupper():
			result += chr((ord(char) - key - ord('A')) % 26 + ord('A'))
		elif char.islower():
			result += chr((ord(char) - key - ord('a')) % 26 + ord('a'))
		else:
			result += char
	return result

print("Welcome to Caesar Cipher!")
choice = input("Do you want to encrypt or decrypt your message? (e/d): ").lower()
if choice == 'e':
	print("We will now encrypt your message...")
	key = int(input("Insert a key: "))
	text = input("Enter a message: ")
	print("Encoded string: " + encrypt(text, key))
elif choice == 'd':
	print("We will now decrypt your message...")
	key = int(input("Insert a key: "))
	text = input("Enter a message: ")
	print("Decoded string: " + decrypt(text, key))