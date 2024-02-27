# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:50:33 2024

Created for SDEV 220 Fall 2024

Author
------
c.s.francis

Description
-----------
A quick example on documentation generators

"""




class Person():
    def __init__(self, name, age, town):
        """
        the constructor for our person object

        Parameters
        ----------
        name : STR
            the name of the person being represented virtually.
        age : INT
            number of years since this person was born.
        town : STR
            place you will most likely find this person.

        Returns
        -------
        None.

        """
        self.name = name
        self.age = age
        self.town = town
        
        
    
    def sentence(self):
        """
        an alternate to-string method, for example purposes

        Returns
        -------
        str
            the sentence describing this person.

        """
        return f"{self.name} lives in {self.town} and is {self.age} years old."
    
    
    def add(self, x, y):
        """
        a method to add two numbers together

        Parameters
        ----------
        x : numeric
            one of the numbers.
        y : numeric
            the other number.

        Returns
        -------
        numeric
            the sum of the two parameters given.

        """
        return x + y
    
    
    def greet(self):
        """
        general system configuration check

        Returns
        -------
        None.

        """
        print("hello world")
        
        
        






if __name__=="__main__":
    p1 = Person("chris", 45, "clarksville")
    
    



