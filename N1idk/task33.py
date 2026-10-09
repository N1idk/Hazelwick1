import random 
number1 = random.randint(0,100)
number2 = random.randint(0,100)
number3 = random.randint(0,100)
number4 = random.randint(0,100)
number5 = random.randint(0,100)

print(number1)

guess1 = int(input("Guess a number between 1 and 100: "))
guess2 = int(input("Guess another number between 1 and 100: "))
guess3 = int(input("Guess another number between 1 and 100: "))
guess4 = int(input("Guess another number between 1 and 100: "))
guess5 = int(input("Guess another number between 1 and 100: "))

ng = abs(number1-guess1)

if ng == 0:
    print("Bang-on")
elif ng <= 5:
    print("Close")
elif ng <= 6 and ng >= 10:
    print("Okay")
elif ng >= 11:
    print("Way off")
# I paused here

ng1 = abs(number2-guess2)

if ng1 == 0:
    print("Bang-on")
elif ng1 <= 5:
    print("Close")

ng2 = abs(number3-guess3)

if ng2 == 0:
    print("Bang-on")
elif ng2 <= 5:
    print("Close")

ng3 = abs(number4-guess4)

if ng3 == 0:
    print("Bang-on")
elif ng3 <= 5:
    print("Close")

ng4 = abs(number5-guess5)

if ng4 == 0:
    print("Bang-on")
elif ng4 <= 5:
    print("Close")