
# export a list of boards to the __init__.py file
# python _rip >> __init__.py in this folder 

import os
import string


def rip():
    boards = {}
    files = os.listdir()
    for i in files:
        short_name = i.split(".")[0]
        if i.endswith(".py"):
            dat = open(i).read().splitlines()
            for j in dat:
                if j.startswith("class"):
                    line = j.split()[1].split("(")[0]
                    if line.endswith("Platform"):
                        boards[short_name] = line
    return boards


boards = rip()
str(boards)

b = 'boards = {:s}'.format(str(boards))
print(b)
