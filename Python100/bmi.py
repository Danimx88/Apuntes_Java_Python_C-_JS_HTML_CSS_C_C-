#
#
#@author Daniel Romero R
#
#
#Body mass index
#
# BMI = (mass kg / height m^2) = ((mass lb / height in^2)) X 703
#
height = input('Enter your height in m: ')
weight = input('Enter your weight in kg: ')

bmi = int(float(weight) / float(height) ** 2) #hegiht * height

print(bmi)
