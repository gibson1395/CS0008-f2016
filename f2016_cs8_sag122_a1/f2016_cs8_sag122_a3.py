global_dictionary = []
mfilename = 'f2016_cs8_a3.data.txt'

mFile = open(mfilename, 'r')

for filename in mFile:
    filename = filename.rstrip('\n')
    file = open(filename, 'r')
    for line in file:
        line = line.strip('\n').split(',')
        name = str(line[0])
        value = float(line[1])
        if name in global_dictionary:
            global_dictionary[name].append(value)
        else:
            global_dictionary[name] = [value]

print(global_dictionary)