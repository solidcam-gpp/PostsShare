from math import *

import time
  
a = 0
b = 0
c = 0
V = 0

#
#LOGGING_ENABLED = True
#
# 
#
#LOG_FILE = "MachSim_SCinfo.xml"

 

#def Load(text):
#
#        f = open(LOG_FILE, "R+")
#
#        f.read(text)
#
#        f.close()
#
# 
#
#def GetID(operation):
#    for line in f:
#       f.readline()
#       if 
#				

class Sub_Machines(object):
    
    VERSION = 1
    TYPE = "move"
    AXIS = ["U1","U2","U3","U","X1","X2","Z1","Z2","Z3","Z4","Z5","Z","X","Z6","Jaws","Y2","Y1"]

    def ProcessMove(self, environment, operation, move):

       move["axisValue"]["U1"] = move["axisValue"]["U"] * 0.25
       move["axisValue"]["U2"] = move["axisValue"]["U"] * 0.5
       move["axisValue"]["U3"] = move["axisValue"]["U"] * 0.75
       
       move["axisValue"]["X1"] = move["axisValue"]["X"] * 0.4
       move["axisValue"]["X2"] = move["axisValue"]["X"] * 1
       
       move["axisValue"]["Z5"] = move["axisValue"]["Z"] * 0.1666 
       move["axisValue"]["Z4"] = move["axisValue"]["Z"] * 0.3333
       move["axisValue"]["Z3"] = move["axisValue"]["Z"] * 0.5
       move["axisValue"]["Z2"] = move["axisValue"]["Z"] * 0.6666
       move["axisValue"]["Z1"] = move["axisValue"]["Z"] * 0.83
       move["axisValue"]["Z6"] = move["axisValue"]["Z"] 


       move["axisValue"]["Y1"] = move["axisValue"]["Jaws"] * 0.5
       move["axisValue"]["Y2"] = move["axisValue"]["Jaws"] * 0.5

out_Sub_Machines = Sub_Machines()
#<preprocessor fileName="preprocessor.py" instance="out_AddNewMoves" /> <!-- coppy this line to .xml (except the #) -->
#<preprocessor fileName="preprocessor.py" instance="out_Sub_Machines" /> <!-- coppy this line to .xml (except the #) -->