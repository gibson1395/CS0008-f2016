length1 = float(input('Enter the length of the first rectangle '))
width1 = float(input('Enter the width of the first rectangle '))
length2 = float(input('Enter the length of the second rectangle '))
width2 = float(input('Enter the width of the second rectangle '))

area_of_rectangle1 = length1 * width1
area_of_rectangle2 = length2 * width2

if area_of_rectangle1 > area_of_rectangle2:
    print('The area of the first rectangle is larger than the second')
elif area_of_rectangle2 > area_of_rectangle1:
    print('The area of the second rectangle is larger than the first')
elif area_of_rectangle1 == area_of_rectangle2:
    print(' The area of both rectangles are the same')

else:
    print('An error occurred in the process')

