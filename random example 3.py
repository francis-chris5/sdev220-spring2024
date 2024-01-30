# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:45:00 2024

@author: franc
"""



import colored

print("Hello world")


colored.Fore.green

print(f"{colored.Fore.green}hello {colored.Fore.cyan}world")

print(f"{colored.Back.yellow} {colored.Fore.black} here's a bee thing {colored.Style.reset}")


import tqdm, time

counter = 0
for i in tqdm.tqdm(range(100)):
    counter += i
    time.sleep(0.1)
    
print(counter)

