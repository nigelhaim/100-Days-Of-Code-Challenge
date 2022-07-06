credit_number = input("Input credit card number: ")

A=1
input_Credit = []
for i in range(0, len(credit_number), A):
    # convert to int, after the slicing process
    input_Credit.append(int(credit_number[i : i + A]))
    
final_Arr = [int(input_Credit) for input_Credit in input_Credit]

total1 = 0
i = 0

while i < (len(final_Arr)):
    toAdd = str(int(final_Arr[i]) * 2)
    if int(toAdd) < 10:
        total1 += int(toAdd)
    else:
        temp = [int(a) for a in toAdd ]
        for j in temp:
            total1 += int(j)
    i+=2

j = 1

while j < len(final_Arr):
    total1 += final_Arr[j]
    j += 2
firstTwo_raw = ""
for i in range(2): 
    firstTwo_raw += str(final_Arr[i])
firstTwo = int(firstTwo_raw)

if total1 != 0:
    if len(final_Arr) == 15 and (firstTwo == 34 or firstTwo == 37):
        print("AMEX")
    
    elif len(final_Arr) == 16 and (firstTwo == 51 or firstTwo == 52 or firstTwo == 53 or firstTwo == 54 or firstTwo == 55):
        print("MASTERCARD")
    elif len(final_Arr) == 13 or len(final_Arr) == 16 and (final_Arr[0] == 4):
        print("VISA")
    else:
        print("INVALID")
        

else:
    print("INVALID")