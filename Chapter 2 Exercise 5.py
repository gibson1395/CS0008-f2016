# speed of car per hour
speed = 90

# speed of car per minute
speed2 = 1.5

# distances traveled
distance1 = 6
distance2 = 10
distance3 = 15

# distance traveled in 145 minutes
# since I have the speed/minute calculation (see column 4)
distance4 = 145

#distance traveled for each travel time
distance1 = float((speed * distance1))
distance2 = float((speed * distance2))
distance3 = float((speed * distance3))
distance4 = float((speed * distance4))

#display kilometers driven with given time
print ('Distance the car will travel in six hours is', distance1)
print ('Distance the car will travel in ten hours is', distance2)
print ('Distance the car will travel in fifteen hours is', distance3)
print ('Distance the car will travel in '
       'two hours and 25 minutes hours is', distance4)