def swap(arr, first, second):
    temp = arr[second]
    arr[second] = arr[first]
    arr[first] = temp
    for i in range(len(arr)):
        print(arr[i])

test = [2,3,4,5,6]
swap(test, 0, 1)