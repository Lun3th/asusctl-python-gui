import tkinter as tk
from tkinter import *
import os
import subprocess
import json
root = tk.Tk()


#Get current values
#Fanspeed init

activemode = subprocess.getstatusoutput('asusctl profile -A')
act = activemode[1].replace('Active profile:', '')
cpuspeedvariable = tk.IntVar()

currFanMode = json.loads(act)['fan_preset']
#1 = boost, 0 = normal, 2 = silent
if (currFanMode == 1):
    cpuspeedvariable.set(1)
    print("Boost")
elif(currFanMode == 0) :
    cpuspeedvariable.set(0)
    print("Normal")
else:
    cpuspeedvariable.set(2)
    print("Silent")
#End of fanspeed init

#Set fanspeed function
def setCpufanSpeed():
    print(cpuspeedvariable.get())
    if(cpuspeedvariable.get() == 2) :
        os.system('asusctl profile silent')
        os.system('asusctl -f silent')
    elif(cpuspeedvariable.get() == 0) :
        os.system('asusctl profile normal')
        os.system('asusctl -f normal')
    else :
        os.system('asusctl profile boost')
        os.system('asusctl -f boost')
#End of set fanspeed function


#Buttons for fanspeed
fanspeedoptions = [ ("Silent", 2),
   	                ("Normal", 0),
    	            ("Turbo", 1)]


tk.Label(root, 
         text="Set Fan speed",
         justify = tk.CENTER,
         padx = 20).pack()

for option, val in fanspeedoptions:
    tk.Radiobutton(root, 
                   text=option,
                   indicatoron = 0,
                   width=20,
                   padx = 20,
                   fg="black",
                   bg="#ad1111",
                   activebackground="#e37676",
                   highlightbackground="#e37676",
                   activeforeground="#420101",
                   variable=cpuspeedvariable, 
                   command=setCpufanSpeed,
                   value=val).pack()



root.mainloop()