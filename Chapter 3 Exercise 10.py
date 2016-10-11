# values of the currencies
penny = .01
nickel = .05
dime = .1
quarter = .25
# have the user enter the quantities
penNum = float(input('Enter the total number of pennies '))
nickelNum = float(input('Enter the total number of nickels '))
dimeNum = float(input('Enter the total number of dimes '))
quarterNum = float(input('Enter the total number of quarters '))
# check to see if the quantities are equal to $1 or more than or less than $1
if (penny * penNum) + (nickel * nickelNum) + (dime * dimeNum) + (quarter * quarterNum) == 1:
    print('Congratulations! You have won the game!')
elif (penny * penNum) + (nickel * nickelNum) + (dime * dimeNum) + (quarter * quarterNum) > 1:
    print('The amount enter was more than a dollar')
elif (penny * penNum) + (nickel * nickelNum) + (dime * dimeNum) + (quarter * quarterNum) < 1:
    print('The amount enter was less than a dollar')
else:
    print('An error occurred')