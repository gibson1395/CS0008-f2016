# create global dictionary
global_dictionary = {}
# name masterfile
mfilename = 'f2016_cs8_a3.data.txt'



# open masterfile
mFile = open(mfilename, 'r')

# create counters
fileCount = 0
lineCount = 0

# loop for reading and opening files then counts how many files read
for filename in mFile:
    filename = filename.rstrip('\n')
    file = open(filename, 'r')
    file.readline()
    fileCount += 1
    for line in file:
        line = line.strip('\n').split(',')
        name = str(line[0])
        value = float(line[1])
        if name in global_dictionary:
            global_dictionary[name].append(value)
        else:
            global_dictionary[name] = [value]
        lineCount += 1
# close files
    file.close()
mFile.close()

# create counter for total distance for the loop
totalDistance = 0

# create for loop to determine the total distance ran
for key in global_dictionary:
    totalDistance += sum(global_dictionary[key])

# create constants
max_value = 0
max_name = ''
min_value = 1000
min_name = ''
numPart = 0

# create empty list
names = []

# create for loop to find mins and maxs of participants and how many are repeated participants
for key in global_dictionary:
    lvalue = global_dictionary[key]
    if max_value < max(lvalue):
        max_value = max(lvalue)
        max_name = key
    if min_value > min(lvalue):
        min_value = min(lvalue)
        min_name = key
    if len(lvalue) > 1:
        numPart += 1
        names.append(key)

# print the results
print('Number of Input files read :', fileCount)
print('Total number of lines read :', lineCount)
print()
print('Total distance run         :', format(totalDistance, '.2f'))
print()
print('Max distance run           :', format(max_value, '.2f'))
print('By participant             :', max_name)
print()
print('Min distance run           :', format(min_value, '.2f'))
print('By participant             :', min_name)
print()
print('Total number of participant:', len(global_dictionary))
print()
print('Number of participants \n '
      'with multiple records     :', numPart)
