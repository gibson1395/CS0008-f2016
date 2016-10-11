color1 = str(input('Enter one primary color: '))
color2 = str(input('Enter another primary color: '))

if color1 == str('red') and color2 == str('blue'):
    print('You get purple')
elif color1 == str('red') and color2 == str('yellow'):
    print('You get orange')
elif color1 == str('blue') and color2 == str('yellow'):
    print('You get green')
elif color1 == str('Red') and color2 == str('Blue'):
    print('You get Purple')
elif color1 == str('Red') and color2 == str('Yellow'):
    print('You get Orange')
elif color1 == str('Blue') and color2 == str('Yellow'):
    print('You get Green')
else:
    print('An error has occurred when inputting color(s)')


