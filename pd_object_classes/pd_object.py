
##########################################################
##########################################################
# description: abstract class that represents any Pd object
#
# autor: jeraman
# date: 03/04/2009
##########################################################
##########################################################

class PdObject:
    def __init__(self, x, y, id):
        self.x=x
        self.y=y
        self.id=id
        
    def move (self, x, y):
        self.x=x
        self.y=y
        
