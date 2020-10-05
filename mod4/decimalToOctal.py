# convert decimal to octal

def convertToOctal(decimal: int):
    res = oct(decimal)
    return res


decimal = int(input(
    "Enter a string of decimal based numbers to be converted to octal based: "))
print("Octal: ", convertToOctal(decimal))
