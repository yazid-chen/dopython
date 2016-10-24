# coding:utf-8
from sys import argv                                        #  argv
from os.path import exists                                  #  exist
script, from_file, to_file = argv                           #  from  、 to

print "copying from %s to %s" % (from_file, to_file)

input = open(from_file)                                     #   打开需要操作文件
indata = input.read()                                       #   读取打开文件数据

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)    #目标文件是否存在  存在返回 ture   不存在返回 false

print "Ready, hit return to continue, Ctrl-c to abort."

raw_input()      # 作用： 等待用户选择  继续 或者 停止

output = open(to_file, 'w')                                 #如果to_file 不存在，那么新建一个
output.write(indata)

print "Alright, all done."

output.close()
input.close()