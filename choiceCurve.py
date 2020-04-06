# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:32:28 2020

@author: antho
"""

def choiceCurve() :
    possibilities = ["sinus", "cosinus", "both"]
    choicesNumbers = [1,2,3]
    while True :
        userInput = input("Do you want a curve using sinus (1), cosinus (2) or both (3) ? ")
        if userInput == "q" :
            break
        try :
            userInputChecked = int(userInput)
            if userInputChecked in choicesNumbers:
                print("you choosed ", userInputChecked, " which corresponds to ", possibilities[userInputChecked-1])
                userInputChecked = possibilities[userInputChecked - 1]
                return userInputChecked
                break
            else :
                print("You did not input the good number")
        except :
            userInputChecked = userInput.lower()
            if userInputChecked in possibilities :
                print("you choosed ", userInput)
                return userInputChecked
                break
            else :
                print ("You did not input a text possibility among the ones proposed.")