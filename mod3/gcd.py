# implement euclids alogrithm

def euclidsAlgo(smaller, larger):

    if smaller == 0:
        return larger
    print("The function will be called again passing " + str((larger % smaller)))
    print(" as the first argument and " + str(smaller) + " as the second")
    return euclidsAlgo(larger % smaller, smaller)


firstNum = int(input("Enter the smaller number: "))
secondNum = int(input("Enter the larger number: "))

print("Calling the function for the first time, it will run recursively until the first argument is 0")

gcd = euclidsAlgo(firstNum, secondNum)

print("The greatest common divisior is " + str(gcd))
