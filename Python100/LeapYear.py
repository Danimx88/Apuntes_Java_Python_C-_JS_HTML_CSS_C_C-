year = int(input("Write the year: "))
if  (year % 4) == 0:  ##the year is %4 = 0, yes next, or else
    if (year % 100) == 0: # if year % 100 = 0  is not a leap year, if !=0 next elif
        if(year % 400) == 0:
            print(f'The {year} is a leap-year')
        else:
            print(f'The year {year} is not a leap-year ')
    elif (year%100) != 0:                       
        print(f'The {year} is a leap-year')
else:
    print(f'The year {year} is not a leap-year ')

