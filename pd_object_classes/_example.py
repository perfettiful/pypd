
##########################################################
##########################################################
# description: test file
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################


from pd_object_collection import *

if __name__ == '__main__':
    poc = PdObjectCollection()
    print "collection of pd objects created successfully"
    print "creating of pd objects itself"
    print "list: " + str(poc.list)
    obj1 = Object(100, 100, 'dac~', 1)
    obj2 = Message(101, 101, 'merda', 2)
    obj3 = Number(102, 102, 3)
    obj4 = Comment(104, 104, 'huhuuhuhu', 4)
    obj5 = Symbol(105, 105, 5)
    poc.create(obj1)
    poc.create(obj2)
    poc.create(obj3)
    poc.create(obj4)
    poc.create(obj5)
    
    print "list: "
    for i in poc.list:
        print i
    
    print "##########################################"
    print "searching an invalid object"
    obj=poc.search(7)
    print obj
    print "searching the first element"
    obj=poc.search(1)
    print obj
    print obj.id
    #print obj.text
    print "##########################################"
      
    print "editing pd objects... (printing before modification/after modification)"
    print obj4
    print obj4.text
    poc.editComment(4, "hahahahaha")
    print obj4
    print obj4.text
    
    print obj1
    print obj1.label
    poc.editObject(1, "osc~ 440")
    print obj1
    print obj1.label
    
    print obj3
    print obj3.value
    poc.incrementNumber(3)
    poc.incrementNumber(3)
    poc.decrementNumber(3)
    print obj3
    print obj3.value

    print obj2
    print obj2.text
    poc.editComment(2, "morda")
    print obj2
    print obj2.text
    
    print "removing all pd objects"
    poc.remove(1)
    poc.remove(2)
    poc.remove(3)
    poc.remove(4)
    poc.remove(5)
    print "list: " +  str(poc.list)
    print "done."
