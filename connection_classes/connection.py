
##########################################################
##########################################################
# description: abstract class that represents any single connection between Pd objects
#
# autor: jeraman
# date: 04/04/2009
##########################################################
##########################################################

class Connection:
    def __init__(self, id_src, id_dest, inlet, outlet):
        self.id_src= id_src
        self.id_dest= id_dest
        self.inlet=inlet
        self.outlet=outlet
        
