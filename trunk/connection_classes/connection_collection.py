
##########################################################
##########################################################
# description: abstract class that represents a collection of connections
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

from connection import *


class ConnectionCollection:
    def __init__(self):
        self.list=[]
    
    
    
    
    #looks for a specific connection
    def search (self, id_src, outlet, id_dest, inlet):
        for c in self.list:
            if c.id_src == id_src and c.id_dest == id_dest and c.inlet == inlet and c.outlet == outlet:
                return c
        return None
    
    
    
    
    #adds a given connection to db       
    def create (self, obj):
        self.list.append(obj)
        
        
        
        
    #removes a given connection from db
    def remove (self, id_src, outlet, id_dest, inlet):
        obj=self.search(id_src, outlet, id_dest, inlet)
        if obj!=None:
            self.list.remove(obj)
            return True
        return False
        
        
        
        
    #looks for the connections of a specific object
    def searchConnectionsOfAnObject (self, id):
        result=[]
        for c in self.list:
            id_str=str(id)    
            if c.id_src == id_str or c.id_dest == id_str:
                result.append(c)
        return result