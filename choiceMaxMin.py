# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:36:44 2020

@author: antho
"""
#Split each loop for a function
#Do it for the radians as well
#Test the whole return

def choiceMaxMin(userChoiceUnit) :
    #Allow the user to choose max min and the split dpending on the type of unit
    if userChoiceUnit == "degree" :
        while True :
            #MINIMUM INPUT
            userMin = input("What degree you want to start with ?")
            if userMin == "q" :
                break
            try :
                userMinChecked = float(userMin)
                break
            except :
                print("You did not choose a number for the min!")
        while True :
            #MAXIMUM INPUT
            userMax = input("What degree you want to finish with?")
            if userMax == "q" :
                break
            try :
                userMaxChecked = float(userMax)
                if userMaxChecked > userMinChecked :
                    break
                else :
                    print("Your maximum ", userMaxChecked, " is inferior to your minimum ", userMinChecked)
            except :
                print("You did not choose a number for the max!")
        while True :
            #JUMP BY INPUT
            userJump = input("What degree you want between 2 points in your graph ? Advice is ", 5.72)
            if userJump == "q" :
                break
            try :
                userJumpChecked = float(userJump)
                if userJumpChecked > userMaxChecked or userJumpChecked > (userMaxChecked - userMinChecked):
                    print("Your jumps are higher than what they should. Decrease them.")
                else :
                    break
            except :
                print("You did not choose a number for the jump!")
                
        print("you choosed degree")
        return [userMinChecked, userMaxChecked, userJumpChecked]
    else :
        while True :
            #minimum
            userMin = input("What radians you want to start with ? (reminder : a circle is 2*pie radians)")
            if userMin == "q" :
                break
            try :
                userMinChecked = float(userMin)
                break
            except :
                print("You did not input a number for the min")
        while True :
            #maximum
            userMax = input("What radians you want to finish with ? (reminder : a circle is 2*pie radians)")
            if userMax == "q" :
                break
            try :
                userMaxChecked = float(userMax)
                if userMaxChecked < userMinChecked :
                    print("Your maximum ", userMaxChecked, " is lower than your minimum ", userMinChecked)
                else :
                    break
            except :
                print ("You did not input a number for the max")
        while True :
            #jump
            userJump = input("What radians you want between 2 points in your graph ? (reminder : a circle is 2*pie radians) Advice is ", 0.1)
            if userJump == "q" :
                break
            try :
                userJumpChecked = float(userJump)
                if userJumpChecked > userMaxChecked or userJumpChecked > (userMaxChecked - userMinChecked):
                    print("Your jumps are higher than what they should. Decrease them.")
                else :
                    break
            except :
                print("You did not choose a number for the jump!")
        return [userMinChecked, userMaxChecked, userJumpChecked]