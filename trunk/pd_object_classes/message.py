
##########################################################
##########################################################
# description: abstract class that represents a message
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

from pd_object import *

class Message (PdObject):
    def __init__(self, x, y, text, id):
        PdObject.__init__(self,x, y, id)
        self.text = text
    
    def edit(self, text):
        self.text=text
        

    
