total = 0
for number in range(1,100):
    if number %2 == 0:
        print(number)
    if number % 3 == 0 and number % 5 == 0:
        print("FiizBuzz")
    elif number %3 == 0:
        print("Fiiz")
    elif number %5 == 0:
        print("Buzz")

for number in range(1,100):
    if number % 3 == 0 and number % 5 == 0:
        print("FiizBuzz")
    elif number %3 == 0:
        print("Fiiz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)
