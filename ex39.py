ten_things = "Apples oranges crows telephone Light sugar"

print "wait there's not 10 things in that list , let's fix that."

stuff = ten_things.split(" ")

more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "there's %d items now." % len(stuff)