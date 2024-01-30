# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:19:16 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""

## lists (dynamic)

myList = [1, 2, "hello world", True, 3.14]
print(myList[2])

myList.append(5)

print(myList)

myList.extend( [7, 2.82, False] )

print(myList)

myList.insert(2, "new thing")

print(myList)


# import sys

# sys.path.insert(0, "../new folder")
# print(sys.path)



## tuples  (static)

## just like a list except cannot change

myTuple = (1, 2, 3, "hello", False, 3.14)

print(myTuple[3])



for item in myList:
    print(item)
    


## sets (no indexing, no order, just the whole list every time)

mySet = {5, 4, True, "words", "random stuff"}

print(mySet)

for s in mySet:
    print(s)



## dictionary (key value pairs instead of indexes)

myDictionary = {"age": 45, "name": "chris", "pets": "goldfish"}

print(myDictionary["age"])


myDictionary["car"] = "patriot"
print(myDictionary)

for d in myDictionary:
    print(myDictionary[d])
    


for i, j in enumerate(myList):
    print(str(i) + "  -- " + str(j))


print("\n\n\n\n*****************\n\n\n")
    
### list comprehensions and generators

# odds = []
# for i in range(100):
#     if i % 2 != 0:
#         odds.append(i)


odds = [i for i in range(100) if i%2 != 0] ## comprehension
print(odds)


notEven = (i for i in range(10000) if i%2 != 0) ## generator

for n in notEven:
    if n % 7 == 0:
        print(n)








#########################



