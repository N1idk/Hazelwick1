score = 0
import random 
number1 = random.randint(0,100)
number2 = random.randint(0,100)
number3 = random.randint(0,100)
number4 = random.randint(0,100)
number5 = random.randint(0,100)

# Remove the hashtags for print commands if u want to test it and see the exact random number
# print(number1)
# print(number2)
# print(number3)
# print(number4)
# print(number5)

guess1 = int(input("Guess a number between 0 and 100: "))
guess2 = int(input("Guess another number between 0 and 100: "))
guess3 = int(input("Guess another number between 0 and 100: "))
guess4 = int(input("Guess another number between 0 and 100: "))
guess5 = int(input("Guess another number between 0 and 100: "))

ng = abs(number1-guess1)

if ng == 0:
    print("Bang-on")
    score = score + 10
elif ng <= 5:
    print("Close")
    score = score + 5
elif ng <= 6 and ng >= 10:
    print("Okay")
    score = score + 2
elif ng >= 11:
    print("Way off")
    score = score + 0

ng1 = abs(number2-guess2)

if ng1 == 0:
    print("Bang-on")
    score = score + 10
elif ng1 <= 5:
    print("Close")
    score = score + 5
elif ng1 <= 6 and ng1 >= 10:
    print("Okay")
    score = score + 2
elif ng1 >= 11:
    print("Way off")
    score = score + 0

ng2 = abs(number3-guess3)

if ng2 == 0:
    print("Bang-on")
    score = score + 10
elif ng2 <= 5:
    print("Close")
    score = score + 5
elif ng2 <= 6 and ng2 >= 10:
    print("Okay")
    score = score + 2
elif ng2 >= 11:
    print("Way off")
    score = score + 0

ng3 = abs(number4-guess4)

if ng3 == 0:
    print("Bang-on")
    score = score + 10
elif ng3 <= 5:
    print("Close")
    score = score + 5
elif ng3 <= 6 and ng3 >= 10:
    print("Okay")
    score = score + 2
elif ng3 >= 11:
    print("Way off")
    score = score + 0

ng4 = abs(number5-guess5)

if ng4 == 0:
    print("Bang-on")
    score = score + 10
elif ng4 <= 5:
    print("Close")
    score = score + 5
elif ng4 <= 6 and ng4 >= 10:
    print("Okay")
    score = score + 2
elif ng4 >= 11:
    print("Way off")
    score = score + 0

print(f"Your total score is {score}!")