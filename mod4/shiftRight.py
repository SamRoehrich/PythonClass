def main():
    string = str(input("Enter a string of bits: "))
    print(leftShift(string))


def leftShift(string :str):
    shift = 4
    front = string[:shift]
    back = string[shift:]
    return back + front
main()