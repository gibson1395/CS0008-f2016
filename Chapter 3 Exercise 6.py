month = int(input('Enter a month in numeric form: '))

day = int(input('Enter a numeric day of the month: '))

year = int(input('Enter the last two digits of a year: '))

if year == day * month:
    print('The date is magic')
else:
    print('The date is not magic')
