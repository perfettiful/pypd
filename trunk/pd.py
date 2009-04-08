
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
    
    
    
    #everytime it happens a change, loads what happened to pd
    def loadFile(self):
        #loads the text from the file
        serverFile = open("communication_classes/server.pd","r")
        #jumping to a specific position
        text=serverFile.read()
        #closing the file
        serverFile.close()
        
        #getting the begining of the pd canvas where the user is working
        aux=text.split("\n#N canvas 0 22 450 300 new 1;")
        #getting the end of the pd canvas where the user is working
        aux=aux[len(aux)-1].split("\n#X restore 122 92 pd new;")
        # separating them by lines
        aux=aux[0].split(";")
        
        #loading the file to memory
        for index in range(len(aux)):
            self.loadLine(aux[index], index)
        
        
    #loads a given pd line to memory   
    def loadLine(self, line, index):
        print line
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
                obj=Symbol(temp[2], temp[3], index)
                
            elif temp[1]=="text":
                aux=temp[4:(len(temp))]
                text=' '.join(aux)
                obj=Comment(temp[2], temp[3], text, index)
            
            #print obj
            self.create(obj)
        
        
if __name__ == "__main__": 
    pd = Pd() 
    pd.loadFile()
    #print pd
    
    for element in pd.poc.list:
        print element
    
    for element in pd.cc.list:
        print element

    #pd.init()
    #pd.finish()
