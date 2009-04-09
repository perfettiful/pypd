import threading
import time

class ThreadOne ( threading.Thread ):

   def run ( self ):

      print 'Thread', self.getName(), 'started.'
      time.sleep ( 5 )
      print 'Thread', self.getName(), 'ended.'

class ThreadTwo ( threading.Thread ):

   def run ( self ):

      print 'Thread', self.getName(), 'started.'
      thingOne.join()
      print 'Thread', self.getName(), 'ended.'

thingOne = ThreadOne()
thingOne.start()
thingTwo = ThreadTwo()
thingTwo.start()



'''
##########################################################
##########################################################
# description: test file
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################


#some variables
x = 10
y = 0
#pd objects list
objects = []



from communication import *



if __name__ == "__main__": 

    #creating a communication object
    pd = Communication() 
    #initializing it
    pd.connectPd() 
    
        
    #main loop - this is the command line ui
    while 1:    
        print "----------------------------------------"
        #printing the objects available in the patch
        print "\navailable objects:"
        for i in range(len(objects)):
            print "* %d - %s"%(i, objects[i])
        
        
        #printing the options the user has
        print "\ndigit your preference ('ctrl + c' to exit):\n"
        print "1 - create an object"
        print "2 - create a message"
        print "3 - create a number"
        print "4 - connect objects"
        print "5 - clean patch"
        
        
        # get what the user wants..
        option = (raw_input("option: "))
        print "----------------------------------------"
        
        
        # if-else that executes whatever the user wants
        if option == "1":
            print "1 - create an object"
            str = raw_input("enter the name of the object: ")
            msg = "pd-new obj %d %d %s" % (x, y, str)
            objects.append("obj "+str)
            x+=1
            y+=1
            print msg
         
            
        elif option == "2":
            print "2 - create a message"
            str = raw_input("enter a content for the message: ")
            msg = "pd-new msg %d %d %s" % (x, y, str)
            objects.append("msg "+str)
            x+=1
            y+=1
            print msg
          
            
        elif option == "3":
            print "3 - create a number"
            msg = "pd-new floatatom %d %d" % (x, y)
            objects.append("floatatom")
            x+=1
            y+=1
            print msg
            
            
        elif option == "4":
            print "4 - connect objects"
            
            obj1 = input("number of the oringin object: ")
            while obj1 >= len(objects) | obj1<0:
                print "enter a valid value"
                obj1 = input("number of the oringin object: ")
                
            let1 = input("number of the outlet: ")
            while let1<0:
                print "enter a valid value"
                let1 = input("number of the outlet: ")
            
            obj2 = input("number of the destination object: ")
            while obj2 >= len(objects) | obj2<0:
                print "enter a valid value"
                obj2 = input("number of the destination object: ")
            
            let2 = input("number of the inlet: ")
            while let2<0:
                print "enter a valid value"
                let2 = input("number of the inlet: ")
                    
            msg = "pd-new connect %d %d %d %d" % (obj1, let1, obj2, let2)
            print msg
            
            
        elif option == "5":
            print "5 - clean patch"
            msg = "pd-new clear"
            objects = []
            print msg
          
          
        else:
            print "invalid option. try again."
            
        #END OF main loop 
            
        #sending a simple message
        pd.sendPd(msg) 
        
    #disconnecting   
    pd.disconnectPd()
'''