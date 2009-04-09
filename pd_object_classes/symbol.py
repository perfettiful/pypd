
##########################################################
##########################################################
# description: abstract class that represents a symbol
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

from pd_object import *

class Symbol (PdObject):
    def __init__(self, x, y, id):
        PdObject.__init__(self,x, y, id)    
        self.symbol="symbol"    
        
    
