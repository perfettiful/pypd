
##########################################################
##########################################################
# description: class that handles pd communication
#
# important: based on Frank Barknecht script at:
# http://markmail.org/message/ohuwrz77hwo3bcwp#query:python%20pdsend+page:1+mid:ybdc6esbu7q53otu+state:results 
#
# autor: jeraman
# date: 06/04/2009
##########################################################
##########################################################

#import sys
from threading  import *
from socket     import *
from time       import *  
from subprocess import *








#variable that stores the port number
PORT = 3000 
#variable that stores the host
HOST = "localhost"
#replace this to where pdsend file is (COMPLETY DIRECTORY)
PD_DIR = "//Applications/audio/Pd-extended.app/Contents/Resources/bin"
#replace this to where server.pd is (COMPLETY DIRECTORY)
SERVER_DIR = "//Users/Jera/Documents/projetos/_pyD/pypd/communication_classes"






# a thread class that we're gonna use for calling the server.pd patch
class RemotePd ( Thread ):
   def run ( self ):
       temp = "cd %s && ./pd -nogui %s/server.pd" %(PD_DIR, SERVER_DIR)
       p = Popen(temp, shell=True)





#communication class
class Communication(socket): 
    #constructor
    def __init__(self, host=HOST, port=PORT): 
        self._port = int(port) 
        self._host = host 
        socket.__init__(self)
        #initializing the server.pd...
        print "initializing server.pd..."
        RemotePd().start()
        sleep(5)
        
    #connecting to pd
    def connectPd(self): 
        try: 
            self.connect((self._host, self._port)) 
            print "connecting with pd"
            return True
        except error, err: 
            print "Error connecting to %s:%d: %s" % (self._host, self._port, err) 
            return False
    
    #sending a command to pd
    def sendPd(self, command):
        try:
            command += ";" 
            self.send(command)
            return True
        except error, err: 
            print "Error sending message %s : %s" % (command, err) 
            return False

    #closing connection
    def disconnectPD(self): 
        self.close() 
        print "closing connection with pd" 
    
    
