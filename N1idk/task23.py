score = 0
equation1 = input("Enter a addition equation: ")
equation2 = input("Enter a subtraction equation: ")
equation3 = input("Enter a multiplication equation: ")
equation4 = input("Enter a division equation: ")
print(" ")
answer1 = int(input(f"Answer the first equation: {equation1}: "))
answer2 = int(input(f"Answer the second equation: {equation2}: "))
answer3 = int(input(f"Answer the third equation: {equation3}: "))
answer4 = int(input(f"Answer the fourth equation: {equation4}: "))
if answer1 == eval(equation1):
    print("Your answer to the first one is correct.")
    score = score + 1
else:
    print("Your answer to the first one is incorrect.")
if answer2 == eval(equation2):
    print("Your answer to the second one is correct.")
    score = score + 1
else:
    print("Your answer to the second one is incorrect.")
if answer3 == eval(equation3):
    print("Your answer to the third one is correct.")
    score = score + 1
else:
    print("Your answer to the third one is incorrect.")
if answer4 == eval(equation4):
    print("Your answer to the fourth one is correct.")
    score = score + 1
else:
    print("Your answer to the fourth one is incorrect.")
print(f"Your score is {score}/4")