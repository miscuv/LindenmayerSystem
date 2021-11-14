#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:20:24 2021

@author: dylan
"""

def LindIter(System, N):
    #set empty value
    LindenmayerString = ""
    #Establish string Tranfrom dictionary with rules for letters
    systemDictionary = {"S":"SLSRSLS","A":"BRARB","B":"ALBLA"}
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

                       
    return LindenmayerString




    