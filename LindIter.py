def LindIter(System, N):
    # global System
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
    print(lindList)  
#def turtlegraph(LindenmayerString)                     
    if System == "Koch":
        kochDic = {"S":f"1/3**{N} ","L":"math.pi/3 ","R":"-2*math.pi/3 "}
        kochTable = lindList.maketrans(kochDic)
        turtleCommands = lindList.translate(kochTable)
    elif System == "Sierpinski":
        sierDic = {"A":f"1/2**{N} ","B":f"1/2**{N} ","L":"math.pi/3 ","R":"-math.pi/3 "}
        sierTable = lindList.maketrans(sierDic)
        turtleCommands = lindList.translate(sierTable)
    # turtleCommands = turtleCommands.split(",")
    
    turtleCommands = turtleCommands.rstrip()
    turtleCommands = turtleCommands.split(" ")               
    return turtleCommands
