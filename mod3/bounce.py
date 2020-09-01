# given the drop height, bounciness index and number of bounces
# calculate the total distance the ball will travel

# UNDONE: LAST INPUT 25, .5, 3 OUTPUT: 66.6666667


def calcBounce(height, bounceIndex, numBounces):
    res = 0.0
    i = 0
    while i < numBounces:
        if i == 0:
            res = height + (height * bounceIndex)
        else:
            res += (((height * bounceIndex) / i) +
                    ((height * bounceIndex) / (i + 1)))
        i += 1
        print(res)
    return res


dropHeight = float(input("Enter the drop height: "))
bouncinessIndex = float(input("Enter the bounciness index: "))
numOfBounces = int(input("How many times can the ball bounce: "))

totalDistance = calcBounce(dropHeight, bouncinessIndex, numOfBounces)

print("The total distance traveled is: " + str(totalDistance) + " units.")
