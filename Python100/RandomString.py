import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#num_item = len(names)

#print(num_item)
#random_choice = random.randint(0, num_item-1)
#print(random_choice)
#print(names_string[random_choice])
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

print(names)
for i in range (1):
    print("The loser is: " + random.choice(names))
