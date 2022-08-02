age = int(input('What is your current age: '))

years = 90
month = 12
weeks = 52
days = 365 #dias en un año
hour = 8_760 #horas por un año
minute = 525_600 # minutos en un año
second = 31_540_000 #segundos en un año
ms = 31_540_000_000 #milisegundos en un año


ryears = years - age
rmonths = (month*years)-(month*age)
rweeks = (weeks*years)-(weeks*age)
rdays = ((days*years)-(days*age))
rhour = (hour*years)-(hour*age)
rminutes = (minute*years)-(minute*age)
rsecond = ((second*years)-(second*age))
print(f'you still have to live {ryears} years, {rmonths} months, {rweeks} weeks, {rdays} days, {rhour} hours , {rminutes} minutes and {rsecond} seconds')
