
##########################################################
##########################################################
# description: the file that manages all pypd stuff
#
# autor: jeraman
# date: 06/04/2009
# v2:27/04/2009
##########################################################
##########################################################



from communication_classes.communication      import *
from connection_classes.connection_collection import *
from pd_object_classes.pd_object_collection   import *

'''
    - create move method 
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
        self.socket.disconnectPd()
    
    
    
    
    
    
    #connecting two objects
    #def connect(self, obj):
    #    self.cc.create(obj)
    def connect(self, obj):
        command="connect %d %d %d %d"%(int(obj.id_src), int(obj.id_dest), int(obj.inlet), int(obj.outlet))
        self.socket.sendPd(command)
    
        self.loadFile()
    
    
    
    
    
    
    #removing a given object
    #def disconnect(self, id_src, id_dest, inlet, outlet):
    #    self.cc.remove(id_src, id_dest, inlet, outlet)
    def disconnect(self, id_src, id_dest, inlet, outlet):
        command="disconnect %d %d %d %d"%(id_src, id_dest, inlet, outlet)
        self.socket.sendPd(command)
        
        self.loadFile()







    #creating a given object
    #def create(self, obj):
    #    self.poc.create(obj)
    def create(self, obj):
        command=None
        
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
        
        self.loadFile()
       
       
       
       
        
 
    #removing a given object by its id
    def remove(self, id):
        text=None

        obj=self.poc.search(id)
        if obj == None:
            return None
        
        if isinstance(obj, Object):
            text=obj.label
            ##############################################
            #lembrar de criar um caso pra quando for gui!!!
            ##############################################
        elif isinstance(obj, Message):
            text=obj.text
        elif isinstance(obj, Number):
            text=str(obj.value)
        elif isinstance(obj, Symbol):
            text=obj.symbol
        elif isinstance(obj, Comment):
            text=obj.text
        
        
        
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
            #print "aiaiai"
            #print count
            i+=1
        self.socket.send("pd-new cut;")
        self.socket.send("pd-new menusave;")
        
        self.loadFile()
    
    
    
    
    #cleans the entire patch, making it blank
    def cleanPatch(self):
        self.socket.sendPd("clear")
        self.socket.sendPd("menusave")
        self.loadFile()
        
    
    
    #method that erases every data in memory
    def resetMemory(self):
        self.poc.list=[]
        self.cc.list =[]

    
    
    #everytime it happens a change, loads what happened to pd
    def loadFile(self):
        #cleans the memory
        self.resetMemory()
        
        text=""
        #reloads till there's a content in the file
        while len(text)==0:
            #loads the text from the file
            serverFile = open("communication_classes/server.pd","r")
            #jumping to a specific position
            text=serverFile.read()
            #closing the file
            serverFile.close()
        
        text=""
        while len(text)==0:
            serverFile = open("communication_classes/server.pd","r")
            text=serverFile.read()
            serverFile.close()
        
        
        text=""
        while len(text)==0:
            serverFile = open("communication_classes/server.pd","r")
            text=serverFile.read()
            serverFile.close()
        
        aux=text.split(";")
        print
        print "1\\\\\\1"
        print aux
        print "1///1"
        print
        
#        if len(aux) > 7:
#            print "######################################" + aux[7]
#            print "######################################"

        aux=aux[7:(len(aux)-4)]
        print
        print "2\\\\\\2"
        print aux
        print "2///2"
        print
        
        for index in range(len(aux)):
            self.loadLine(aux[index], index)
        

       
       
       
        
        
    #loads a given pd line to memory   
    def loadLine(self, line, index):
        #print "line: " + line
        #print

        temp=line.split()
        
        obj=None
        
        #in this case don't do anything
        if len(temp) <= 2:
            #sprint "error: line smaller than 2"
            return
        
        if temp[1]=="connect":
            obj=Connection(temp[2], temp[3], temp[4], temp[5])
            print obj
            self.cc.create(obj)
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
                self.poc.create(obj)
        
        
        
        
        
    ########################################
    ########################################
    # TODO - edit objects
    # TODO - move objects
    ########################################
    ########################################
    
    #edit a specific object
    def edit(self, id, newObj):
        #1- busca o objeto (objVelho) pelo id
        #    a- se nao encontrou, retorna erro
        #    b- se encontrou, retorne objNovo
        #2 - para cada conexao existente, verifica se ela envolve o objVelho encontrado
        #    a- caso sim, armazena em connectionsTemp  
        #3 - remove objVelho da lista de objetos existentes 
        #4 - adiciona objNovo da lista de objetos existentes
        #5 - realiza todas as conexoes de objVelho em objNovo 
        
        #1
        oldObj=self.poc.search(id)
        
        #1- a and b
        if oldObj==None:
            print "Error editing object " + id
            return None
        #2
        result=self.cc.searchConnectionsOfAnObject(id)
        
        #vai aparecer um BUG aqui.
        #o text enviado deve ser igual ao do oldObj encontrado!!! 
        #essa restricao pode ser feita em 1
        #3
        self.remove(oldObj.id)
        
        #vai aparecer um BUG aqui.
        #verificar se a modificacao foi adequada!!!
        #4
        self.create(newObj)
        
        #5
        newObj.id=id
        for c in result:
            self.connect(c)
            