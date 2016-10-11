mass = float(input('Enter the mass of the object: '))
weight = (mass * 9.8)

if weight >= 100 and weight <= 500:
    print('The weight of the object is sufficient')
elif weight < 100:
    print('The weight of the object is too light')
elif weight > 500:
    print('The weight of the object is too heavy')
else:
    print('An error occurred')