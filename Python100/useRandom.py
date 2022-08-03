import random

a = random.randint(0, 10)
print(f"El número aleatorio entre 0 a 10 es: '{a}' ")
b = random.randrange(0, 10, 2)
print(f"El número aleatorio entre 0 a 10 que va de 2 es: '{b}'")
c = random.random() * 5     #randon.randon is for float betwen 0 to 0.999999
print(c)
love_score = random.randint(0, 100)
print(f'Your love score is: {love_score}')

print("Empty or full")
emptyOrFull = random.randint(0, 1)
if emptyOrFull == 1:
    print("The box is full")
else:
    print("The box is empty")
