# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:01:21 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""

import abc


class Animal(metaclass=abc.ABCMeta):
    
    conversion_factor = 2.2 ## class variable/datafield

    def __init__(self, name, age, weight):
        self.name = name ## datafield
        self.__age = age  ## mangled variable/datafield
        self.__weight = weight / Animal.conversion_factor
        
    @abc.abstractmethod
    def makeSound(self):
        pass
        
        
    def get_name(self):
        return self.name
    
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
        return f"{self.get_name()} is {self.get_age()} and weighs"  + format(self.get_weight(), ".1f") + f" kilograms and goes {self.makeSound()}."
        
        

    
class Lion(Animal):
    def makeSound(self):
        return "ROAR!!!"


    
class Cat(Animal):
    
    def makeSound(self):
        return "meow"
    



class Dog(Animal):
    
    def __init__(self, bandanna=False, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.bandanna = bandanna

    def makeSound(self):
        return "Woof!"


class Fish(Animal):
    def makeSound(self):
        return "boop"



if __name__=="__main__":
    
    nemo = Fish("nemo", 1, 0.5)
    print(nemo)
    fido = Dog(name="Fido", age=7, weight=34, bandanna=True)
    print(fido)



