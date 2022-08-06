print("Welcome to the Game")
name = input("Enter your name: ")
age = input("Enter your age: ")
nationality = input("Enter your nationality: ")
city = input("Enter your city")

print(f"Welcome {name}, please confirm your information: \n"
      f"Name: {name}\n"
      f"Age: {age}\n"
      f"Nationality{nationality}\n"
      f"City: {city}")

confirm = input("Please to confirm just enter Y, if the information is incorrect enter an N: ")

if confirm == "y":
    print("Thanks for your visit")

elif  confirm != "y":
        print("Please")

qorC= input("if you don't want to continue just enter the Q, or C to continue: ")

if qorC == "q" or qorC == "Q":
    print("Thanks, see you later :D ")
elif qorC != "q" or qorC !="Q":
    print("Thanks, Now let's continue ")


