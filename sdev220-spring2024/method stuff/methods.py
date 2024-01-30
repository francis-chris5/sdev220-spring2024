# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:29:37 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""



## this is not procedural
x = 3
y = "hello world"
z = x**2


## "return functions"
def SayHi():
    return y
## end SayHi()


def aBunch():
    return 4, 5, 6, "a", "b", "c"

## "void functions"
def hello():
    print(y)
## end hello()


def labels(parameter):
    calc = parameter * 2
    if calc > 5:
        print("doubling that is kind of big")
    else:
        while calc > 0:
            print("that's kind of small")
            calc -= 1


## nested function
def inside(stuff):
     if isinstance(stuff, str):
         print("that will work")
         
         def nesting():
             print(stuff)
             
     else:
         def nesting():
             print("that's the wrong type")
         
     nesting()
     
     
## closure
def giving(stuff, things):
    print(things)
    
    def changing():
        modified = stuff[1:-2]
        return modified
    
    return changing()
     
     
## decorators
from functools import wraps
import datetime
 
def signature(func):
    @wraps(func)
    def whoIsIt(*args, **kwargs):
        print("c.s.francis made this on " + str(datetime.datetime.now()) )
        return func(*args, **kwargs)
    
    return whoIsIt

import time
def timed(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time_ns()
        func(*args, **kwargs)
        end = time.time_ns()
        duration = end - start
        print(f"it took {duration} nanosecond to do that")
        return 
    return wrapped

@signature
def double(x):
    return 2 * x

@signature
@timed
def add(x, y):
    return x + y


@timed
def subtract(x, y):
    return x - y






## "guard statement"
if __name__ == "__main__":
    result = SayHi()
    print(result)

    x, y, z, w, u, v = aBunch()
    print(x)
    print("as well as " + str(u) + " " + str(z))

    argument = 7 ## arguments fill parameters
    labels(argument)
    argument = 2
    labels(argument) ## send an argument to fill a parameter

    inside("words")
    
    inside(3)
    
    print(giving("here are some words", 17))
    
    print(double(4))

    print(add(3, 4))
    
    print(subtract(7, 2))






























#######################################
