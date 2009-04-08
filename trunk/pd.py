
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

'''
    - remove connection doesn't work
    - when the process ends, pd thread remains running
    - create example of Pd classs
'''

class Pd:
    #constructor
    def __init__(self):
        self.socket = Communication() 
        self.cc     = ConnectionCollection()
        self.poc    = PdObjectCollection()
        
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
    #def disconnect(self, id_src, id_dest, inlet, outlet):
    #    self.cc.remove(id_src, id_dest, inlet, outlet)
    
    #creating a given object
    def create(self, obj):
        self.poc.create(obj)
    
    #removing a given object by its id
    #def remove(self, id):
    #    self.poc.remove(id)
    
    def remove(self, id, text):
        count=0
        for obj in self.poc.list:
            comp=None
            if isinstance(obj, Object):
                comp=obj.label
                ##############################################
                #lembrar de criar um caso pra quando for gui!!!
                ##############################################
            elif isinstance(obj, Message):
                comp=obj.text
            elif isinstance(obj, Number):
                comp=str(obj.value)
            elif isinstance(obj, Symbol):
                comp=obj.symbol
            elif isinstance(obj, Comment):
                comp=obj.text
            
            if text==comp:
               count+=1 
            
            if obj.id==id:
                break
            
        self.socket.send("pd-new find %s;"%(text))
        i=1
        while i<count:
            self.socket.send("pd-new findagain;")
            print "aiaiai"
            print count
            i+=1
        self.socket.send("pd-new cut;")
        self.socket.send("pd-new menusave;")
            
            
    
    #moving a given object
    def move(self, id, x, y):
        self.poc.move(id, x, y)

        
    ########################################
    ########################################
    # TODO - edit objects
    ########################################
    ########################################
    
    
    
    #everytime it happens a change, loads what happened to pd
    def loadFile(self):
        #loads the text from the file
        serverFile = open("communication_classes/server.pd","r")
        #jumping to a specific position
        text=serverFile.read()
        #closing the file
        serverFile.close()
        
        #getting the begining of the pd canvas where the user is working
        aux=text.split("\n#N canvas 0 22 737 328 new 1;")
        #print aux
        #getting the end of the pd canvas where the user is working
        aux=aux[len(aux)-1].split("\n#X restore 122 92 pd new;")
        # separating them by lines
        aux=aux[0].split(";")
        
        #loading the file to memory
        for index in range(len(aux)):
            self.loadLine(aux[index], index)
        
        
    #loads a given pd line to memory   
    def loadLine(self, line, index):
        temp=line.split()
        obj=None
        
        #in this case don't do anything
        if len(temp) <= 2:
            #sprint "error: line smaller than 2"
            return
        
        if temp[1]=="connect":
            obj=Connection(temp[2], temp[3], temp[4], temp[5])
            self.connect(obj)
        else:
            if temp[1]=="obj":
                aux=temp[4:(len(temp))]
                label=' '.join(aux)
                obj=Object(temp[2], temp[3], label, index) 
                
                ##############################################
                #lembrar de criar um caso pra quando for gui!!!
                ##############################################
                
            elif temp[1]=="msg":
                aux=temp[4:(len(temp))]
                text=' '.join(aux)
                obj=Message(temp[2], temp[3], text, index)
                
            elif temp[1]=="floatatom":
                obj=Number(temp[2], temp[3], index)
                
            elif temp[1]=="symbolatom":
                aux=temp[4:(len(temp))]
                text=' '.join(aux)
                obj=Symbol(temp[2], temp[3], text, index)
                
            elif temp[1]=="text":
                aux=temp[4:(len(temp))]
                text=' '.join(aux)
                obj=Comment(temp[2], temp[3], text, index)
            
            #print obj
            if obj!=None:
                self.create(obj)
        
        
if __name__ == "__main__": 
    pd = Pd() 
    pd.loadFile()
    pd.init()
    
    
    
    '''
    ######## removing 1! #########
    for element in pd.poc.list:
        print element.label
    
    pd.remove(2, "osc~ 440")
    
    for element in pd.poc.list:
        print element.label
    
    ######## removing 2! #########
    for element in pd.poc.list:
        print element.label
    
    pd.remove(1, "osc~")
    
    for element in pd.poc.list:
        print element.label
    
    ######## removing 3! #########
    for element in pd.poc.list:
        print element.label
    
    pd.remove(0, "dac~")
    
    for element in pd.poc.list:
        print element.label
    '''
    
    pd.finish()
    print "done."

    
    #print pd
    
    #for element in pd.poc.list:
    #    print element
    
    #for element in pd.cc.list:
    #    print element

    #pd.init()
    #pd.finish()
