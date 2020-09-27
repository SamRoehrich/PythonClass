# Edit the code below

theSum = 0.0
numbers = []
data = input("Enter a number: ")
theAverage = 0.0
while data != "":
    number = float(data)
    numbers.append(number)
    theSum += number
    data = input("Enter the next number: ")
print("The sum is", theSum)
theAverage = theSum / len(numbers)
print("The average of the numbers is", theAverage)
