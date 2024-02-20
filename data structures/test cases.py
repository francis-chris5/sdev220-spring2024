# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:33:38 2024

Created for SDEV 220 Fall 2024

@author: c.s.francis

"""




from structures import MyList, MyStack, MyQueue





if __name__=="__main__":
    x = MyList(3)
    x.add(4)
    x.add(5)
    x.add(6)
    print(x)
    x.remove(5)
    print(x)
    print("\n\n******************\n\n")
    s1 = MyStack()
    s1.push(5)
    s1.push(7)
    print(s1)
    x = s1.pop()
    print("twice as much as the top of the stack is " + str(2 * x))
    print(s1)
    s1.push(3)
    s1.push(23)
    s1.push(33)
    print(s1)
    while not s1.is_empty:
        x = s1.pop()
        print(s1)
    print("\n\n******************\n\n")
    q1 = MyQueue()
    q1.offer(3)
    q1.offer(4)
    print(q1)
    x = q1.poll()
    print(x)
    print("three times as much as the \
 first element in the queue is " + str(3*x))
    print(q1)
    q1.offer(6)
    q1.offer(7)
    q1.offer(8)
    print(q1)
    while not q1.is_empty:
        q1.poll()
        print(q1)



