
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
    cc.create(Connection(1, 1, 1, 0))
    cc.create(Connection(1, 2, 1, 0))
    cc.create(Connection(1, 3, 1, 0))
    cc.create(Connection(1, 4, 1, 0))
    print "list: "
    for i in cc.list:
        print i
        
    print "removing all pd objects"
    cc.remove(1, 1, 1, 0)
    cc.remove(1, 2, 1, 0)
    cc.remove(1, 3, 1, 0)
    cc.remove(1, 4, 1, 0)
    
    print "list: " +  str(cc.list)
    print "done."