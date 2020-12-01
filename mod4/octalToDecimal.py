# convert octal to decimal

def octalToDecimal(octal: oct):
    return int(octal)


octal = input("Enter an octal number: ")
print("The decimal version of that number is: ", str(octalToDecimal(octal)))
