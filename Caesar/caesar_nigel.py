key = -1
while(key <= 0 or key >= 999):
    key = int(input("Insert a key: "))

input_String = input("plaintext: ")
input_list = [c for c in input_String]
cyphered_string = ""

for i in input_list:
    if i.isalpha():
        if i.isupper():
            cyphered_string += chr((((ord(i) - 65) + key) % 26) + 65)
        elif i.islower():
            cyphered_string += chr((((ord(i) - 97) + key) % 26) + 97)
    else:
        cyphered_string += i
        
print(cyphered_string) 