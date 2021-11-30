# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:18:18 2021

@author: Asus
"""

import numpy as np
from matplotlib import pyplot as plt
import math as math

def LindIter(System, N):

    #set empty value
    LindenmayerString = ""
    #Establish string Tranfrom dictionary with rules for letters
    systemDictionary = {"S":"SLSRSLS","A":"BRARB","B":"ALBLA","D":"DLDDRDL"}
    #creates translation table
    rulesTable = LindenmayerString.maketrans(systemDictionary)
    #Initiates Koch sequence
    if System == 1:
        #establishes initial conditions for Koch
        LindenmayerString = "S"
        for i in range(N):
            LindenmayerString = LindenmayerString.translate(rulesTable)
    #initiates Sierpinski sequence
    elif System == 2:
        #establishes initial conditions for Siepinski
        LindenmayerString = "A"
        for i in range(N):
            LindenmayerString = LindenmayerString.translate(rulesTable)

    LindList = LindenmayerString

    return(LindList,System,N)  

def turtlegraph(lindList, System, N):
    turtleCommands = ''          
    if System == 1:
        kochDic = {"S":f"1/3**{N} ","L":f"np.pi/3 ","R":f"-2*np.pi/3 "}
        kochTable = lindList.maketrans(kochDic)
        turtleCommands = lindList.translate(kochTable)
    elif System == 2:
        sierDic = {"A":f"1/2**{N} ","B":f"1/2**{N} ","L":f"np.pi/3 ","R":f"-np.pi/3 "}
        sierTable = lindList.maketrans(sierDic)
        turtleCommands = lindList.translate(sierTable)
    
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
            angle = np.dot(np.array([[np.cos(eval(comd)),-np.sin(eval(comd))],\
                                     [np.sin(eval(comd)),np.cos(eval(comd))]],),angle)
        else:
            coords = np.append(coords,[np.add(np.array(coords[-1]),\
                                              np.dot(angle,steps),dtype=float)],axis = 0)
        xs=[x[0] for x in coords]
        ys=[x[1] for x in coords]
    plt.plot(xs,ys)
    plt.show()
    
def Main():
    while True:

        # Define menu items
        # menuItems = np.array(["Choose the type of Lindenmayer system and the number of\
        #               iterations", "Generate plot", "Quit"])
        print("1.Choose the type of Lindenmayer system and the number of iterations")
                      
        print("2.Generate plot")
        print("3.Quit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            System = int(input("Choose the type of Lindenmayer system:\n 1.Koch System\n 2.Sierpinski System \n "))
            N = int(input("Choose the number of iterations: "))
            if System != 1 and System != 2:
                print('There is no such type of Lindenmayer system!')
            print(LindIter(System, N))
        if choice == 2:
            if N <= 0:
                print('The number of iterations must be positive!')
            if N > 8:
                print('To prevent excessive run-time, the number of iterations is limited to 8.')
            if System == 0 or N == 0:
                print('You have not selected a system or number of iterations.')
            LindList = LindIter(System, N)
            turtlePlot(turtlegraph(LindList[0],LindList[1],LindList[2]))
        if choice == 3:
            print('Bye-Bye!')
            break
Main()
            
                
            
            
            
            
        
              

    