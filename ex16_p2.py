from sys import argv

script, filename = argv

target = open(filename, 'w')

line1 = "chenyw"

line2 = "qwerty-"

line3 = "herakels"

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()