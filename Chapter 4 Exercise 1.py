# This program calculates the total number of calories burned
# after 10, 15, 20, 25, and 30 minutes

print('Minutes\tBurned')
for time in range(10, 31, 5):
    burned = time * 4.2
    print(time, '\t', burned)
