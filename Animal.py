# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:01:21 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""



class Animal():
    
    x = 2.2 ## class variable/datafield

    def __init__(self, name, age, weight):
        self.name = name ## datafield
        self.__age = age  ## mangled variable/datafield
        self.__weight = weight
        
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
        
    def get_weight(self):
        return self.__weight
        
        
    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.__weight == other.get_weight()
        else: 
            return False
        
        
    def __str__(self): ## or __repr__()
        return f"{self.name} is {self.__age} and weighs {self.__weight}"
        
        

    








if __name__=="__main__":
    pass



