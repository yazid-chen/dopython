from sys import argv
script, filename = argv
target = open(filename,'w')

line1 = "I am blind but not deaf"
line2 = "good better best"

target.write(line1)
target.write(line2)

target.close()