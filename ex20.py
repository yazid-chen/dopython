from sys import argv
script, input_file = argv
# 读取文件的信息
def print_all(f):
    print f.read()
#  指定文件读取的位置
def rewind(f):
    f.seek(0)
#  输出 文件共有多少行
def print_a_line(line_count, f):
    print line_count, f.readline()
# 打开当前文件
current_file = open(input_file)

print ""
# 定位到当前文档的开始位置
rewind(current_file)

print ""

current_line = 1

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)