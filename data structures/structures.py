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
        
    def get_element(self):
        return self.element
    
    def set_element(self, element):
        self.element = element
        
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next
        
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
    
    


class MyStack(MyList):
    def __init__(self):
        super().__init__(None)
        self.is_empty = True
    ## end of constructor
        
    
    def push(self, element):
        if self.get_element() == None:
            self.is_empty = False
            super().__init__(element)
            return
        self.is_empty = False
        self.add(element)
        return
    
    def pop(self):
        current = self
        if current.get_next() == None:
            self.is_empty = True
            temp = current.get_element()
            current = None
            return temp
        while current.get_next() != None:
            current = current.get_next()
        temp = current.get_element()
        self.remove(current.get_element())
        return temp
    
    
    
class MyQueue(MyList):
    def __init__(self):
        super().__init__(None)
        self.is_empty = True
    ## end of constructor
    
    
    def offer(self, element):
       if self.get_element() == None:
           self.is_empty = False
           super().__init__(element)
           return
       self.is_empty = False
       self.add(element)
       return 
    
    def poll(self):
        current = self
        if current.get_next() == None:
            self.is_empty = True
            return current.get_element()
        current = self.get_next()
        temp = self.get_element()
        self.set_element(current.get_element())
        self.set_next(current.get_next())
        return temp
    
    
class MyNode():
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        

class MyBST():
    def __init__(self, node):
        self.node = node ## this needs to be a MyNode object
        
    
    def add(self, root, node):
        if node.element < root.element:
            if root.left == None:
                root.left = node
                return
            self.add(root.left, node)
        elif node.element > root.element:
            if root.right == None:
                root.right = node
                return
            self.add(root.right, node)
        
    
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print("<<<---   " + str(root.element) + "    --->>>") 
            self.inOrder(root.right)
    
            
    def preOrder(self, root):
        if root != None:
            print("<<<---   " + str(root.element) + "    --->>>")
            self.preOrder(root.left)
            self.preOrder(root.right)
      
        
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("<<<---   " + str(root.element) + "    --->>>")







if __name__=="__main__":
    ## [7, 11, 3, 5, 19, 14, 32, 8, 2]
    tree = MyBST(MyNode(7))
    tree.add(tree.node, MyNode(11))
    tree.add(tree.node, MyNode(3))
    tree.add(tree.node, MyNode(5))
    tree.add(tree.node, MyNode(19))
    tree.add(tree.node, MyNode(14))
    tree.add(tree.node, MyNode(32))
    tree.add(tree.node, MyNode(8))
    tree.add(tree.node, MyNode(2))
    print("in order")
    tree.inOrder(tree.node)
    print("\n\n\npre order")
    tree.preOrder(tree.node)
    print("\n\n\npost order")
    tree.postOrder(tree.node)
    

    
    



















