##########################################################
##########################################################
# description: test file
#
# autor: jeraman
# date: 08/05/2009
##########################################################
##########################################################


#id variable
id = 0



from pd import *



if __name__ == "__main__": 

    #creating a communication object
    pd = Pd() 
    #initializing it
    pd.init() 
    
    exit=False
        
    #main loop - this is the command line ui
    while not exit:    
        pd.loadFile()
        print "----------------------------------------"
        #printing the objects available in the patch
        print "\navailable objects:"
        for i in range(len(pd.poc.list)):
            print "* %d - %s"%(i, pd.poc.list[i])
        
        #printing the connections available in the patch
        print "\navailable connections:"
        for i in range(len(pd.cc.list)):
            print "* %d - %s"%(i, pd.cc.list[i])
        
        #printing the options the user has
        print "\ndigit your preference ('ctrl + c' to exit):\n"
        print "1 - create an object"
        print "2 - create a message"
        print "3 - create a number"
        print "4 - connect objects"
        print "5 - remove object"
        print "6 - clean patch"
        print "7 - exit"
        
        
        # get what the user wants..
        option = (raw_input("option: "))
        print "----------------------------------------"
        
        
        
        
        # now if-else that executes whatever the user wants
        #first... if the user wants to create a object...
        if option == "1":
            print "1 - create an object"
            str = raw_input("enter the name of the object: ")
            obj = Object(0, 0, str, id)
            pd.create(obj)
            id+=1
        
        
        
        
            
        #if the user wants to create a message...
        elif option == "2":
            print "2 - create a message"
            str = raw_input("enter a content for the message: ")
            obj = Message(0, 0, str, id)
            pd.create(obj)
            id+=1
          
            
            
            
            
        #if the user wants to create a number...
        elif option == "3":
            print "3 - create a number"
            obj = Number(0, 0, id)
            pd.create(obj)
            id+=1
            
            
            
            
            
        #if the user wants to connect objects...
        elif option == "4":
            print "4 - connect objects"
            
            obj1 = input("number of the oringin object: ")
            while obj1 >= len(pd.poc.list) | obj1<0:
                print "enter a valid value"
                obj1 = input("number of the oringin object: ")
                
            let1 = input("number of the outlet: ")
            while let1<0:
                print "enter a valid value"
                let1 = input("number of the outlet: ")
            
            obj2 = input("number of the destination object: ")
            while obj2 >= len(pd.poc.list) | obj2<0:
                print "enter a valid value"
                obj2 = input("number of the destination object: ")
            
            let2 = input("number of the inlet: ")
            while let2<0:
                print "enter a valid value"
                let2 = input("number of the inlet: ")
                    
            c1 = Connection(obj1, let1, obj2, let2)
            pd.connect(c1)
            




            
        #if the user wants to remove a object...
        elif option == "5":
            print "5 - remove object"
            print "enter the id of the object you want to remove"

            id = input("number of the inlet: ")
            while id >= len(pd.poc.list) | id<0:
                print "enter a valid value"
                id = input("number of the inlet: ")
            
            pd.remove(id)



            
            
        #if the user wants to clean the patch...
        elif option == "6":
            print "7 - clean patch"
            pd.cleanPatch()




          
        #if the user wants to exit the program...
        elif option == "7":
            print "8 - exit"
            #disconnecting   
            pd.finish()
            exit=True
          
        else:
            print "invalid option. try again."
            
        #END OF main loop 
        
