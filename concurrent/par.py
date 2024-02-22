# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:56:04 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""



import multiprocessing as mp

asyncResults = []

def collectResults(res):
    asyncResults.append(res)


def busyWork(x):
    result = ""
    while x > 0:
        result += "the busy work has been carried out " + str(x) + " times\n"
        x -= 1
        return result
        
def tedious(y):
    result = ""
    for i in range(y):
        result += "doing more stuff " + str(i) + "\n"
    return result
    

if __name__=="__main__":
    cores = mp.Pool(mp.cpu_count())
    
    syncResult = cores.apply(busyWork, args=[6])
    print(syncResult)
    print("*****************\n")
    mapResult = cores.map(tedious, [9])
    print(mapResult)
    print("******************\n")
    
    
    stuff = cores.apply_async(busyWork,  args=[7], callback=collectResults)
    
    print("doing unrelated things here")
    
    cores.close()
    cores.join()
    
    
    print(asyncResults)
    
    



