# create function calculation
def calculation():
    # have u ser enter the distance and assign to local variable distance
    distance = float(input('Enter a distance in kilometers '))
    # convert to miles
    miles = distance * (.6214)
    # print the distance in miles with two decimals
    print('The distance in miles is', format(miles, '.2f'))
# call the function
calculation()
