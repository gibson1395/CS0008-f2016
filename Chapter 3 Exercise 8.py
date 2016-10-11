people = int(input('Enter the number of guests attending the cookout '))
hotdogs = int(input('Enter the number of hot dogs each guest will eat: '))

numberDogs = hotdogs * people
buns = (numberDogs % 8)
dogs = (numberDogs % 10)
buns1 = int(numberDogs // 8)
dogs1 = int(numberDogs // 10)


if buns == 0:
    print('The minimum number of buns needed', buns1)
else:
    print('The minimum number of buns needed is', (buns1 + 1))

if dogs == 0:
    print('The minimum number of hot dogs needed', dogs1)
else:
    print('The minimum number of hot dogs needed is', (dogs1 + 1))

print('The number of buns that will be left over is', buns)
print('The number of hot dogs that will be left over is', dogs)


