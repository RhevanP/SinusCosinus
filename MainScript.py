# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:03:11 2020

@author: antho
"""
#Goals :
#1) Learn Panda package
#2) Generate sinus and cosinus data
#3) Generate sinus and cosinus graphs
#4) Let the user decide what to see

import numpy as np
import math
#import matplotlib as mpl
import matplotlib.pyplot as ppl
import choiceUnit as cU
import choiceCurve as cC
import choiceMaxMin as cMM

#input user : cos or sin or both, max min

userChoiceUnit = cU.choiceUnit() #return either degree or radians
userChoiceCurve = cC.choiceCurve() #return ["sinus", "cosinus", "both"]
userChoiceMaxMin = cMM.choiceMaxMin(userChoiceUnit) #return [userMinChecked, userMaxChecked, userJumpChecked]

#Transform everything into radians
if (userChoiceUnit == "degree") :
    for number in userChoiceMaxMin :
        number = math.radians(number)
        print(number)

#Draw graph
x = np.arange(userChoiceMaxMin[0], userChoiceMaxMin[1], userChoiceMaxMin[2])
if userChoiceCurve == "sinus" :
    y = np.sin(x)
    ppl.plot(x,y)
    ppl.show()
elif userChoiceCurve == "cosinus" :
    z = np.cos(x)
    ppl.plot(x,z)
    ppl.show()
else : 
    y = np.sin(x)
    z = np.cos(x)
    ppl.plot(x,y,x,z)
    ppl.show()
