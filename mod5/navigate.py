def printLines(lines):
    print("The file has " + str(len(lines)) + " lines.")
    line = input("Enter a line to print[0 to quit]: ")
    if int(line) == 0 or int(line) > len(lines):
        print("Good bye.")
        exit()
    elif int(line) != 0:
        print(str(line) + str(lines[int(line) - 1]))
        printLines(lines)


fileName = input("Enter the file name: ")

# open and parse file
file = open(fileName)
data = file.readlines()

printLines(data)
