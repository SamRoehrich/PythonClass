# convert octal to decimal

def octalToDecimal(octal):
    return str(int(oct(octal)))


octal = input("Enter an octal number: ")
print("The decimal version of that number is: ", octalToDecimal(octal))
