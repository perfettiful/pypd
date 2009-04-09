
##########################################################
##########################################################
# description: abstract class that manages all Pd object available
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

from object import *
from message import *
from number import *
from symbol import *
from comment import *



class PdObjectCollection:
    def __init__(self):
        self.list=[]
        
    #returns a given object
    def search(self, id):
        for obj in self.list:
            if (id == obj.id):
                return obj
        else:
            return None
    
    ######## create function #######
    
    def create(self, obj):
        self.list.append(obj)
    
    
    ######## remove function #######
    def remove (self,id):
        obj=self.search(id)
        if obj!=None:
            self.list.remove(obj)
            return True
        return False
    

    ######## edit functions #######
        
    #edits a object
    def editObject(self, id, label):
        obj=self.search(id)
        if obj!=None:
            obj.edit(label)
            return True
        return False
            
    #edits a message
    def editMessage(self, id, text):
        obj=self.search(id)
        if obj!=None:
            obj.edit(text)
            return True
        return False
    
    #edits a comment
    def editComment(self, id, text):
        obj=self.search(id)
        if obj!=None:
            obj.edit(text)
            return True
        return False
    
    #increments a number
    def incrementNumber(self, id):
        obj=self.search(id)
        if obj!=None:
            obj.increment()
            return True
        return False

    #increments a number
    def decrementNumber(self, id):
        obj=self.search(id)
        if obj!=None:
            obj.decrement()
            return True
        return False
    
    
    ######## move function #######
    def move(id, x, y):
        obj=self.search(id)
        if obj!=None:
            obj.move(x, y)
            return True
        return False
    
