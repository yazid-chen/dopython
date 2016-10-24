from sys import argv

script, filename = argv

target = open(filename,'r')

line1 = target.read()

line2 = target.read()

line3 = target.read()

print line1, line2, line3