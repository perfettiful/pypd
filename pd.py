
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
    - create example of Pd classs
'''

class Pd:
    #constructor
    def __init__(self):
        self.socket = Communication() 
        #you should comment the following lines
        self.cc     = ConnectionCollection()
        self.poc    = PdObjectCollection()
        
        
    #initializing the pd api - must be called before working with it
    def init(self):
        self.socket.connectPd()
        
        
    #finishing a pd api session - must be called after working with it
    def finish(self):
        self.socket.disconnectPD()
    
    
    #connecting two objects
    #def connect(self, obj):
    #    self.cc.create(obj)
    def connect(self, obj):
        command="connect %d %d %d %d"%(int(obj.id_src), int(obj.id_dest), int(obj.inlet), int(obj.outlet))
        self.socket.sendPd(command)
    
    
    #removing a given object
    #def disconnect(self, id_src, id_dest, inlet, outlet):
    #    self.cc.remove(id_src, id_dest, inlet, outlet)
    def disconnect(self, id_src, id_dest, inlet, outlet):
        command="disconnect %d %d %d %d"%(id_src, id_dest, inlet, outlet)
        self.socket.sendPd(command)


    #creating a given object
    #def create(self, obj):
    #    self.poc.create(obj)
    def create(self, obj):
        command=None
        
        #"The sum of 1 + 2 is {0}".format(1+2)
        
        if isinstance(obj, Object):
            command = "obj %d %d %s" % (int(obj.x), int(obj.y), obj.label)
            ##############################################
            #lembrar de criar um caso pra quando for gui!!!
            ##############################################
        
        elif isinstance(obj, Message):
            command="msg %d %d %s"%(int(obj.x), int(obj.y), obj.text)

        elif isinstance(obj, Number):
            command="floatatom %d %d"%(obj.x, obj.y)
        
        elif isinstance(obj, Symbol):
            command="symbolatom %d %d %s"%(obj.x, obj.y, obj.symbol)
        
        elif isinstance(obj, Comment):
            command="text %d %d %s"%(obj.x, obj.y, obj.text)
        
        self.socket.sendPd(command)
        
 
    #removing a given object by its id
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
            
            
    
    ########################################
    ########################################
    # TODO - edit objects
    # TODO - move objects
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
    obj1 = Object(100, 100, "dac~", 0)
    obj2 = Object(100, 100, "osc~ 440", 1)
    
    c1=Connection(obj2.id, 0, obj1.id, 0)
    
    pd.create(obj1)
    pd.create(obj2)
    pd.connect(c1)
    
    sleep(3)
    pd.disconnect(c1.id_src, c1.id_dest, c1.inlet, c1.outlet)
    '''
    
    
    '''
    
    obj1 = Object(100, 100, 'dac~', 0)
    obj2 = Message(101, 101, 'merda', 1)
    obj3 = Number(102, 102, 2)
    obj4 = Comment(104, 104, 'huhuuhuhu', 3)
    obj5 = Symbol(105, 105, 4)
    
    pd.create(obj1)
    pd.create(obj2)
    pd.create(obj3)
    pd.create(obj4)
    pd.create(obj5)
    
    pd.remove(obj1.id, obj1.label)
    pd.remove(obj2.id, obj2.text)
    pd.remove(obj3.id, obj3.value)
    pd.remove(obj4.id, obj4.text)
    pd.remove(obj5.id, obj5.symbol)
    
    '''
    
    
    
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
