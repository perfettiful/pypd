
##########################################################
##########################################################
# description: abstract class that represents a Number
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

from pd_object import *

class Number (PdObject):
    def __init__(self, x, y, id):
        PdObject.__init__(self,x, y, id)
        self.value=0
    
    def increment(self):
        self.value+=1
    
    def decrement(self):
        self.value-=1
        

    
