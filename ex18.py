# coding: utf-8

def print_two(*args):
    arg1, arg2 = args
    print "%d and %d" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "%d and %d" % (arg1, arg2)

def print_three(*args):
    arg1, arg2, arg3 = args
    print "%d + %d + %d = %d" % (arg1, arg2, arg3, arg1+arg2+arg3)

print_two(1, 2)

print_two_again(1, 2)

print_three(1 ,2 ,3)
    