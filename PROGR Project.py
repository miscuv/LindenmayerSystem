import numpy as np
from matplotlib import pyplot as plt
import math as math
""" Welcome to the Lindenmayer System Program we created for our exam project!
    We chose this project because it looked interesting and seemed like a good
    way to combine some things we had learned in Math 1 this semester as well
    as what we learned in programming.
    
    Lindenmayer systems were created to model natural systems using simple and 
    iterable rules. This program will display a couple of these systems: Koch and
    Sierpinski.
    
    What this program does is it first asks you to select a Lindenmayer system.
    Then it will ask for a number of iterations. 
    NOTE! The number of iterations is limited to prevent excessive 
    computational runtime.
    Then the program will give you the option to plot the system. This will 
    display a plot with the selected Lindenmayer System
    
    Enjoy!
    
     -Veronica, Alex and Dylan
"""
"""
This function takes the inputs of System(Koch or Sierpinski) and N(iterations)
and creates a string based on a series of rules which correspond to each system.
These rules are stored in a dicitonary.
created by: Dylan Bailey s215228@dtu.dk
"""
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
"""
This function takes the inputs LindList, System and N and converts the
string of letters given by LindIter into step lengths and angles which 
correspond to the rules of the system. The return is a string of step 
lengths and angles called turtleCommands

created by:     Dylan Bailey s215228@dtu.dk
"""
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
 """
 This function takes the string turtleCommands and converts the step length and
 turn angle into a series of coordinates which can then be plotted.
 
 created by:    Dylan Bailey 215228@dtu.dk

 """
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
        xs=[x[0] for x in coords] #set the values for the x axis of the plot to be the first column of the coordinates
        ys=[x[1] for x in coords] #set the values for the x axis of the plot to be the second column of the coordinates
    plt.plot(xs,ys) #plot the coordinates
    plt.show() #show the plot
  
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
            
                
            
            
            
            
        
              

    
