# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:53:35 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""


# handler = open("testing123.txt", "w")
# handler.write("hello world\nthat's all for now\n")
# handler.close()

## w for over-write
## a for append
## r for read

with open("testing123.txt", "w") as handler:
    handler.write("I prefer this syntax\n when writing files \n\t in python")

with open("testing123.txt", "r") as readHandler:
    for line in readHandler:
        print(line)
        

x = 3
y = "Hello world"
z = True


with open("myData.sdev", "w") as toFile:
    toFile.write(str(x))
    toFile.write(str(y))
    toFile.write(str(z))
    
    
### later

with open("myData.sdev", "r") as fromFile:
    x2 = fromFile.readline()
    y2 = fromFile.readline()
    z2 = fromFile.readline()
    
print(x2, y2, z2)



bunchOfData = [43, 12, 99, 75, 88, 13]
moreData = ["a", "b", "c"]

import csv
with open("bunchOfData.csv", "w") as toFile:
    writer = csv.writer(toFile)
    writer.writerow(bunchOfData)
    writer.writerow(moreData)


with open("bunchOfData.csv", "r") as fromFile:
    reader = csv.reader(fromFile)
    for row in reader:
        if len(row) != 0:
            print(row)
        


someData = [
    {"name": "sally", "age": "23", "town": "salem"},
    {"name": "chuck", "age": "58", "town": "charlestown"},
    {"name": "lewis", "age": "14", "town": "louisville"},
    ]

import json

with open("someData.json", "w") as toFile:
    toFile.write(json.dumps(someData))
    

with open("someData.json", "r") as toFile:
    x = json.loads(toFile.read())
    print(x)



















##############################3 white space for scrolling
