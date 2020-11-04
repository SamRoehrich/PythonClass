def isSorted(list):
    if len(list) < 2:
        return True
    if len(list) > 1:
        x = 0
        y = 1
        while list[y] > list[x]:
            if y == len(list) - 1:
                return True
            else:
                x = y
                y += 1
        return False

def main():
    lyst=[]
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))


main()
