
##########################################################
##########################################################
# description: abstract class that represents a gui element
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################


'''
mensagem que contém todos os parâmetros a serem implementados!

bang
#X obj 88 33 bng 15 250 50 0 empty empty empty 17 7 0 10 -262144 -1 -1;

toogle
#X obj 130 28 tgl 15 0 empty empty empty 17 7 0 10 -262144 -1 -1 0 1;

#X obj 173 27 nbx 5 14 -1e+37 1e+37 0 0 empty empty empty 0 -8 0 10 -262144 -1 -1 0 256;

vertical slider
#X obj 253 26 vsl 15 128 0 127 0 0 empty empty empty 0 -9 0 10 -262144 -1 -1 0 1;

horizontal slider
#X obj 295 22 hsl 128 15 0 127 0 0 empty empty empty -2 -8 0 10 -262144 -1 -1 0 1;

vertical radio
#X obj 449 44 vradio 15 1 0 8 empty empty empty 0 -8 0 10 -262144 -1 -1 0;

horizontal radio
#X obj 480 38 hradio 15 1 0 8 empty empty empty 0 -8 0 10 -262144 -1 -1 0;

vu
#X obj 617 40 vu 15 120 empty empty -1 -8 0 10 -66577 -1 1 0;

canvas
#X obj 223 224 cnv 15 100 60 empty empty empty 20 12 0 14 -233017 -66577 0;







isso será o próximo módulo!!!

from pd_object import *

class GUI (Object):
    #the gui is initialized with his default values
    def __init__(self, x, y, type, width=15, height=128, value_botton=0, value_top=100, log=0, init=0, send_symbol="empty", receive_symbol="empty", label="empty", x_offset=0, y_offset=-9, font=0, font_size=10, bgd_color=-262144, n1=-1, n2=-1, n3=0, n4=1):
        Object.__init__(self,x, y, type)
        self.width=width
        self.height=height
        self.value_botton=value_botton
        self.value_top=value_top 
        self.log=log
        self.init=init
        self.vsend_symbol="vsend_symbol 
        self.receive_symbol=receive_symbol 
        self.label=label
        self.x_offset=x_offset
        self.y_offset=y_offset 
        self.font=font
        self.font_size=font_size 
        self.bgd_color=bgd_color 
        self.n1=n1 
        self.n2=n2 
        self.n3=n3 
        self.n4=n4
      
    def edit(self, width=15, height=128, value_botton=0, value_top=100, log=0, init=0, send_symbol="empty", receive_symbol="empty", label="empty", x_offset=0, y_offset=-9, font=0, font_size=10, bgd_color=-262144, n1=-1, n2=-1, n3=0, n4=1):
        Object.edit(self,self.type)
        self.width=width
        self.height=height
        self.value_botton=value_botton
        self.value_top=value_top 
        self.log=log
        self.init=init
        self.vsend_symbol=vsend_symbol 
        self.receive_symbol=receive_symbol 
        self.label=label
        self.x_offset=x_offset
        self.y_offset=y_offset 
        self.font=font
        self.font_size=font_size 
        self.bgd_color=bgd_color 
        self.n1=n1 
        self.n2=n2 
        self.n3=n3 
        self.n4=n4  
    
'''        

    
