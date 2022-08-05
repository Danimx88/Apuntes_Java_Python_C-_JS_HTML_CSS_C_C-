a = 0
b = 1
sum = 0
for n in range (1, 100):
    sum = a + b
    print(sum)
    b += 1
    a = sum
