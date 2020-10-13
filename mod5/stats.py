def mean(numbers, len):
    res = 0
    for i in range(0, len):
        res += numbers[i]
    return float(res/len)


def mode(numbers, len):
    maxElem = max(numbers)
    countLen = maxElem + 1
    count = [0] * countLen

    # initialize count array
    for i in range(countLen):
        count[i] = 0

    for i in range(len):
        count[numbers[i]] += 1

    mode = 0
    x = count[0]
    for i in range(1, countLen):
        if(count[i] > x):
            x = count[i]
            mode = i

    return mode


def median(numbers, len):
    sortedNum = sorted(numbers)

    if len % 2 != 0:
        return float(sortedNum[len/2])

    return float((sortedNum[int((len-1)/2)] + sortedNum[int(len/2)]) / 2.0)


def main():
    userList = [3, 1, 7, 1, 4, 10]
    listLen = len(userList)
    calculatedMedian = median(userList, listLen)
    calculatedMode = mode(userList, listLen)
    calculatedMean = mean(userList, listLen)
    print("Median: " + str(calculatedMedian))
    print("Mode: " + str(calculatedMode))
    print("Mean: " + str(calculatedMean))


main()
