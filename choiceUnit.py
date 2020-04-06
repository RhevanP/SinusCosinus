# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:50:31 2020

@author: antho
"""
def choiceUnit () :
    possibilities = ["degree", "radians"]
    choicesNumbers = [1,2]
    while True :
        userInput = input("Do you want to work in degree (1) or radians (2) ? ")
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