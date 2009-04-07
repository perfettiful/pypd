
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
    #constructor
    def __init__(self):
        socket = Communication() 
        cc     = ConnectionCollection()
        poc    = PdObjectCollection()
        
    #initializing the pd api - must be called before working with it
    def init(self):
        self.socket.connectPd()
        
    #finishing a pd api session - must be called after working with it
    def finish(self):
        self.socket.disconnectPD()
    
    #connecting two objects
    def connect(self, obj):
        self.cc.create(obj)
    
    #removing a given object
    def disconnect(self, id_src, id_dest, inlet, outlet):
        self.cc.remove(id_src, id_dest, inlet, outlet)
    
    #creating a given object
    def create(self, obj):
        self.poc.create(obj)
    
    #removing a given object by its id
    def remove(self, id):
        self.poc.remove(id)
    
    #moving a given object
    def move(self, id, x, y):
        self.poc.move(id, x, y)

        
    ########################################
    ########################################
    # TODO - edit objects
    ########################################
    ########################################
    
    def loadFile(self):
    
        
if __name__ == "__main__": 
    pd = Pd() 
    
    
