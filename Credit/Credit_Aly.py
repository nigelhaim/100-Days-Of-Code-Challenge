'''
100 Days of Code -- Day 7
Credit Card Validation -- CS50
Alyza Paige L. Ng
'''
#count length
def count_length(number):
    length = len(str(number))
    if length != 13 and length != 15 and length != 16:
        print("This number is invalid!")
        exit()
    return length
    
#check validity
def valid_num(number):
    list_of_digits = list(str(number))
    list1 = list2 = []
    #range(second to the last digit, skip the first index, every other element) = (start, stop (exclusive), step)
    for i in range(len(list_of_digits) - 2, -1, -2):
        by_two = int(list_of_digits[i]) * 2
        #if the product has 2 digits, add the digits and append in the list
        if by_two > 9:
            by_two_list = list(str(int(by_two)))
            by_two_product = int(by_two_list[0]) + int(by_two_list[1])
            list1.append(by_two_product)
        else:
            list1.append(by_two)
    
    #range(last digit, skip the first index (0 will be excluded), every other element)
    for i in range(len(list_of_digits) - 1, -1, -2):
        list2.append(int(list_of_digits[i]))

    #add both lists and divide by 2 (// will result in integer division only, and idk why the return is doubled)
    return (sum(list1) + sum(list2)) // 2

#get first 2 digits
def start_digits(number):
    return int(str(number)[:2])

#get number
while True:
    try:
        number = int(input("Enter your credit card number: "))
    except ValueError:
        print("Your input must contain only digits!\n")
    else:
        break

#if last digit ends in a '0', print card type
if valid_num(number) % 10 == 0:
    print("Credit Card Type: ", end="")
    if count_length(number) == 16 and (start_digits(number) >= 51 and start_digits(number) <= 55):
        print("MASTERCARD")
    elif count_length(number) == 15 and (start_digits(number) == 34 or start_digits(number) == 37):
        print("AMEX")
    elif int(str(number)[:1]) == 4:
        print("VISA")

#otherwise, print "invalid"
else:
    print("This number is invalid!")