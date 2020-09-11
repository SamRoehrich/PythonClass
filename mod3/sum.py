# take input from the user
# while the input is still a number continue accepting input
# If they press enter quit the loop and
# calculate the sum and average of the numbers entered

from typing import NewType


def getInput(userInput, prevInputs):
    def calcResults(userInputs):
        for i in userInputs:
            print(userInputs[i])
    if userInput == "":
        calcResults(prevInputs)
        return "You have reached the end, congrats?"
    if type(userInput) != int & type(userInput) != str:
        return "You tried entering something that was neither 0-9 nor Enter and broke the program, try again"
    else:
        prevInputs.append(input)
        nextNumber = input("Enter a nunber or press Enter to exit the loop")
        getInput(nextNumber, prevInputs)


getInput(0, [])
