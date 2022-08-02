print("----------------------------------------Welcome to the tip calculator-------------------------\n")
bill = float(input("What was the total bill?: "))
tip = float(input("What percentage tip would you like to give (10%, 12% 0r 15%)?: "))
peope = int(input("How many people to split the bill?: "))
#(percentage x value) / 100

percentage = float((float(tip) * int(bill)) / 100)
total = (percentage + bill)
split = float(float(total) / float(peope))
print(f'Each person should pay: {split}$ usd')
pesos = (float(split) * float(20.45))
print(f'In mexican pesos is equal to {pesos}$ pesos')
