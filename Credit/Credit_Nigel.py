creditNum = -1
validInput = False
while(validInput == False):
    try:
        creditNum = int(input("Input the credit card: "))
        validInput = True
    except:
        print("Input integers only!")

creditNumS = str(creditNum)
coll = [int(a) for a in str(creditNumS)]

cc_number = (int(coll[(len(creditNumS) - 2)])) % 10

