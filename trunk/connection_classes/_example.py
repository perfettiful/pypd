
##########################################################
##########################################################
# description: test file
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################


from connection_collection import *

if __name__ == '__main__':
    cc = ConnectionCollection()
    print "collection of connections created successfully"
    print "creating of connections itself"
    print "list: " + str(cc.list)
    cc.create(Connection(1, 0, 1, 0))
    cc.create(Connection(1, 0, 2, 0))
    cc.create(Connection(1, 0, 3, 0))
    cc.create(Connection(1, 0, 4, 0))
    print "list: "
    for i in cc.list:
        print i
        
        
    result = cc.searchConnectionsOfAnObject(3)
    print "\nresult of searchConnectionsOfAnObject for 3: "
    for i in result:
        print i
        
    result = cc.searchConnectionsOfAnObject(1)
    print "\nresult of searchConnectionsOfAnObject for 1: "
    for i in result:
        print i
        
    result = cc.searchConnectionsOfAnObject(5)
    print "\nresult of searchConnectionsOfAnObject for a inexistent object: "
    for i in result:
        print i
        
    print "\nremoving all pd objects"
    cc.remove(1, 0, 1, 0)
    cc.remove(1, 0, 2, 0)
    cc.remove(1, 0, 3, 0)
    cc.remove(1, 0, 4, 0)
    
    print "list: " +  str(cc.list)
    print "done."