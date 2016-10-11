# This program calculates the number of acres in the tract

# Get the number of square meters of land from the user
square_meters = float(input('Enter the total square meters of land: '))

# Take the number of square meters the user entered
# divided by number of square meters in an acre
total_number_of_acres = square_meters / 4046.8564224

# print the total number of acres the user has
print ('The total number of acres is: ' +
       format(total_number_of_acres, '.2f'))
