
##########################################################
##########################################################
# description: the file that manages all pypd stuff
#
# autor: jeraman
# date: 06/04/2009
##########################################################
##########################################################



from communication_classes.communication      import *
from connection_classes.connection_collection import *
from pd_object_classes.pd_object_collection   import *



class Pd:
    def __init__(self):
        print "criei comunicacao"
        c = Communication() 
        print "criei conexoes"
        cc  = ConnectionCollection()
        print "criei pd objects"
        poc = PdObjectCollection()

if __name__ == "__main__": 
    pd = Pd() 
    
    
