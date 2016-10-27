# coding: utf-8

cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jacksonville'}   # 三个城市

cities['NY'] = 'New York'    #  添加  一个城市

cities['OR'] = 'Portland'    # 添加 第二个城市


def find_city(themap, state):
    '''
    在 themap 中查找state是否存在
    如果存在，则 返回  themap[state]  state的全称
    如果没有找到，则，返回“Not found"
    '''
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention
#
cities['_find'] = find_city

while True:
    print "state? (enter to quit)",
    state = raw_input("> ")
    if not state: break

    # this line is the most important ever! study!

    city_found = cities['_find'](cities, state)

    print city_found