age = int(input("Enter a person's age in years: "))

if age <= 1 and age > 0:
    print('He or she is an infant')
elif age >=2 and age <=12:
    print('He or she is a child')
elif age >=13 and age <=19:
    print('He or she is a teenager')
elif age >=20:
    print('He or she is an adult')
else:
    print('Invalid age given')

