# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:41:22 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""

import threading

def busyWork(x):
    while x > 0:
        print("the busy work has been carried out " + str(x) + " times")
        x -= 1
        
def tedious(y):
    for i in range(y):
        print("doing more stuff " + str(i))
    



if __name__=="__main__":
    first = threading.Thread(target=busyWork, args=(6,))
    second = threading.Thread(target=tedious, args=(9,))
    
    first.start()
    second.start()
    
    first.join()
    second.join()
    
    print("finished")



