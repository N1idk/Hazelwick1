temp = int(input("Enter a number of celsius"))

if temp < 0 :
    print("Freezing")
elif temp <= 20 :
    print("Cold")
elif temp < 30 :
    print("Warm")
elif temp > 30 :
    print("Hot")