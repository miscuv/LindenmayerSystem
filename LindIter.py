import numpy as np
from matplotlib import pyplot as plt
import math as math
def LindIter(System, N):
    # print(System)
    # print(N)
    #set empty value
    LindenmayerString = ""
    #Establish string Tranfrom dictionary with rules for letters
    systemDictionary = {"S":"SLSRSLS","A":"BRARB","B":"ALBLA","D":"DLDDRDL"}
    #creates translation table
    rulesTable = LindenmayerString.maketrans(systemDictionary)
    #Initiates Koch sequence
    if System == "Koch":
        #establishes initial conditions for Koch
        LindenmayerString = "S"
        for i in range(N):
            LindenmayerString = LindenmayerString.translate(rulesTable)
    #initiates Sierpinski sequence
    elif System == "Sierpinski":
        #establishes initial conditions for Siepinski
        LindenmayerString = "A"
        for i in range(N):
            LindenmayerString = LindenmayerString.translate(rulesTable)
    # print(System)
    # print(N)

    lindList = LindenmayerString
    
    # return(lindList,System,N)  

# def turtlegraph(lindList):             
    if System == "Koch":
        kochDic = {"S":f"1/3**{N} ","L":f"np.pi/3 ","R":f"-2*math.pi/3 "}
        kochTable = lindList.maketrans(kochDic)
        turtleCommands = lindList.translate(kochTable)
    elif System == "Sierpinski":
        sierDic = {"A":f"1/2**{N}","B":f"1/2**{N} ","L":f"math.pi/3 ","R":f"-math.pi/3 "}
        sierTable = lindList.maketrans(sierDic)
        turtleCommands = lindList.translate(sierTable)
    # turtleCommands = turtleCommands.split(",")
    
    turtleCommands = turtleCommands.rstrip()
    turtleCommands = turtleCommands.split(" ")  
           
    return turtleCommands

def turtlePlot(turtleCommands):
    coords = np.array([[0,0]])
    steps = np.array([eval(turtleCommands[0]),0], dtype = float)
    angle = np.array([[1,0],[0,1]], dtype = float)


   
    for comd in turtleCommands:
        # Our commands are always step, turn, step, turn .... step. So startin
        # at 0 each odd index is a turn and each even index is a step
        if eval(comd)**2 > 1 :
            print(eval(comd))
            angle = np.dot(np.array([[np.cos(eval(comd)),-np.sin(eval(comd))],\
                                     [np.sin(eval(comd)),np.cos(eval(comd))]],),angle)
        else:
            print(eval(comd))
            coords = np.append(coords,[np.add(np.array(coords[-1]),\
                                              np.dot(angle,steps),dtype=float)],axis = 0)
        
    print(coords)
