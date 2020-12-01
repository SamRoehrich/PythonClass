def main():
    string = str(input("Enter a string of bits: "))
    print(rightShift(string))


def rightShift(string :str):
    shift = 2
    front = string[shift:]
    back = string[:shift]
    return front + back

main()