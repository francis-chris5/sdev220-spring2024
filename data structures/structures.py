# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:30:32 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""



class MyList:
    def __init__(self, element):
        self.element = element
        self.next = None
        
    def add(self, el):
        current = self
        while current.next != None:
            current = current.next
        current.next = MyList(el)
        
        
        
    def remove(self, el):
        current = self
        
        if el == current.element:
            temp = current.next
            self = temp
            
        while current.next.element != el and current.next != None:
            current = current.next
         
        if current.next == None:
            return
        else:
            temp = current.next.next
            current.next = temp
            return
            
        
    def __repr__(self):
        current = self
        string = "["
        while current != None:
            string += str(current.element) + ", "
            current = current.next
            
        string += "]"
        return string
    
    











if __name__=="__main__":
    x = MyList(3)
    x.add(4)
    x.add(5)
    x.add(6)
    print(x)
    x.remove(5)
    print(x)
    
    
    
    



















