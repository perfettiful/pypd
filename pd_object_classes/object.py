
##########################################################
##########################################################
# description: abstract class that represents a object
#
# autor: jeraman
# date: 03/04/2009
##########################################################
##########################################################

from pd_object import *

class Object (PdObject):
    def __init__(self, x, y, label, id):
        PdObject.__init__(self,x, y, id)
        self.label = label
    
    def edit(self, label):
        self.label=label
        

    
