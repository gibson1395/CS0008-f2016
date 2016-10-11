# have user enter temperature
temperature = float(input('Enter the temperature in degrees Fahrenheit '))
# conversion into celsius
celsius = float(5 * (temperature - 32) / 9)
# display the current temperature in celcius
print('The current temperature in degrees Celsius: ' + format(celsius, '.2f'))