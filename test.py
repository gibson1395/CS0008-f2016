# have the user enter which system they would like to use
system = str(input('Would you like to use USC or Metric: '))
# have the user enter the distance and gas used for their appropriate system
distance = float(input('Enter the distance driven: '))
gasUsed = float(input('Enter the gasoline used: '))

# USC to metric:
metricDistance = float(format(distance * 1.60934, '9.3f'))
metricGas = float(format(gasUsed * 3.78541, '9.3f'))

# Metric to USC
usDistance = float(format(distance * 0.621371, '9.3f'))
usGas = float(format(gasUsed * 0.264172, '9.3f'))
# depending on which system the user
# entered, those numbers will be converted to the other system
if system == str('USC'):
    print('The distance driven in kilometers is', metricDistance)
    print('The liters of gasoline used is', metricGas)
elif system == str('Metric'):
    print('The distance driven in miles is', usDistance)
    print('The gallons of gasoline used is', usGas)
else:
    print('An error occurred')

# fuel consumption rating
fuelConsumptionUSA = float(format(usDistance / usGas, '9.3f'))
fuelConsumptionMetric = float(format(((100 * metricGas) / metricDistance), '9.3f'))
# print the fuel consumption rating
print('The fuel consumption in miles per gallon:', fuelConsumptionUSA)
print('The fuel consumption in liters per 100 kilometers:', fuelConsumptionMetric)
# give the consumption rating a category based on 1/100Km
if fuelConsumptionMetric > 20:
    print('The gas consumption rating is extremely poor')
elif fuelConsumptionMetric < 15 and fuelConsumptionMetric <= 20:
    print('The gas consumption rating is poor')
elif fuelConsumptionMetric < 10 and fuelConsumptionMetric <= 15:
    print('The gas consumption rating is average')
elif fuelConsumptionMetric < 8 and fuelConsumptionMetric <= 10:
    print('The gas consumption rating is good')
elif fuelConsumptionMetric <= 8:
    print('The gas consumption rating is excellent')
else:
    print('An error occurred')