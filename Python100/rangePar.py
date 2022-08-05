#a = 0
#b = 1
#sum = 0
#for n in range (1, 101):
#    sum = a + b
#    print(sum)
#    b += 1
#    a = sum

#total = 0
#for number in range (1, 101):
#    total+= number
#    print(" total " + total)

total = 0
b = 0
for number in range (1, 101):
    total = number
    if total %2 == 0:
        a = total
        b += a
print(f"b = {b}")

total2 = 0
for number in range (2 , 101, 2):
    total2 += number
print(total2)
