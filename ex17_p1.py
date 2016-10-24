from sys import argv
script, from_file, to_file = argv
input = open(from_file).read()
output = open(to_file,'w').write(input)
print "OK!"