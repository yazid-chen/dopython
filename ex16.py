# coding:utf-8 #

from sys import argv

script, filename = argv

print "we are going to erase %r." % filename   # 获取清除的文件名称

print "if you don't want that, hit Ctrl-C(^C)." # 取消操作

print "if you do want that, hit RETURN."  #

raw_input("?")

print "Opening the file..."

target = open(filename,'w')  # w 写入操作

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."

target.close()



