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



def divide(a, b):
    """
    

    Parameters
    ----------
    a : int
        the numerator.
    b : int
        the denominator, CANNOT BE ZERO.

    Returns
    -------
    int
        the quotient.
    int
        the remainder.

    """
    return a//b, a%b







if __name__=="__main__":
    x, y = divide(174, 16)
    print(x, y)



