# have the user enter desired cookie amount
number_of_cookies = int(input('How many cookies would you like to make '))

# these are the calculations for sugar butter and flour per cookie
sugar_per_cookie = 6.25
butters_per_cookie = 5
flour_per_cookie = 6.875

# this is the grams needed per cookie multiplied by the desired cookie total
grams_of_sugar_needed = format(sugar_per_cookie * number_of_cookies, '.2f')
grams_of_butter_needed = format(butters_per_cookie * number_of_cookies, '.2f')
grams_of_flour_needed = format(flour_per_cookie * number_of_cookies, '.2f')

# display the grams needed for each ingredient
print('Total grams of sugar needed:', grams_of_sugar_needed)
print('Total grams of butters needed:', grams_of_butter_needed)
print('Total grams of flour needed:', grams_of_flour_needed)


