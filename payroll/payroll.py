# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:20:13 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""


from functools import wraps
import datetime

#@todo payroll calculator: 
    #get name and hours and rate, 
    #calc overtime or not, 
    #and 14% tax



def logger(func):
    @wraps(func)
    def logging(*args, **kwargs):
        with open("payroll_log.log", "a") as log:
            log.write("just ran the " + func.__name__ + " function.\n")
        return func(*args, **kwargs)
    return logging



@logger
def getInputs():
    name = input("Yeah, see... The boss he wants to know your name, see... ") # 1920's mobster prompt
    hours = float(input("GIMME YOUR HOURS!!!! " )) # cheerlearder prompt
    rate = float(input("Nah, how much you make doc? "))
    return name, hours, rate

@logger
def calculateGross(hours, rate):
    if hours > 40:
        gross = (hours-40) * rate * 1.5 + 40 * rate
    else:
        gross = hours * rate
    return gross


@logger
def deductTaxes(gross, tax_bracket):
    deduction = gross * tax_bracket
    net = gross - deduction
    return net


@logger
def printCheck(net, name):
    with open(name + "_check.txt", "w") as toFile:
        toFile.write("\t\t" + str(datetime.datetime.today())[0:10] + "\n\n")
        toFile.write("pay to the order of: \t" + name + "\n")
        toFile.write("Amount: $ \t" + format(net, ".2f"))






    









if __name__=="__main__":
    name, hours, rate = getInputs()
    gross = calculateGross(hours, rate)
    net = deductTaxes(gross, 0.14)
    printCheck(net, name)
    
    
    



