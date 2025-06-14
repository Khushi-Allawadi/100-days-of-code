#bill calculator
bill = float(input("What's the bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give?"))
owe = bill * (1 + tip/100)/people
owe = round(owe, 2)
print("You owe me: ", owe)
