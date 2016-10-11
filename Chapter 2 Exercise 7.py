one_mile = 1.60934 #kilometers
one_gallon = 3.78541 #liters

miles_used = float(input('Enter number of miles driven '))
gallons_used = float(input('Enter number of gallons used driven '))

liters_used = format(gallons_used * one_gallon, '.2f')
kilometers_driven = format(miles_used * one_mile, '.2f')

print('Liters used: ' + str(liters_used))
print('Kilometers driven: ' + str(kilometers_driven))

fuel_consumption = (100 * liters_used)

