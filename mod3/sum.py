# take input from the user
# while the input is still a number continue accepting input
# If they press enter quit the loop and
# calculate the sum and average of the numbers entered

from typing import NewType

Input = NewType("UserInput", int | str)


def getInput(input: Input, prevInputs):
    if input != type(int) & input == "":
        # calcResults(prevInputs)
        return "You have reached the end, congrats?"
    if input != type(int) & input != "":
        return "You tried entering something that was neither 0-9 not Enter and broke the program, try again"
    else:
        prevInputs.append(input)
        nextNumber = int(
            input("Enter a nunber or press Enter to exit the loop"))
        getInput(nextNumber, prevInputs)


getInput(0, [])
