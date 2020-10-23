def decimalToRep(integer, base):
    hexTable = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    if integer != 0:
        number = ""
        while integer > 0:
            remainder = integer % base
            integer = integer // base
            number = hexTable[remainder] + number
            return number
    else:
        return 0
    
def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 16))
    print(decimalToRep(10, 2))

main()