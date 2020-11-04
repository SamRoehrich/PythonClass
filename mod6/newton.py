import math

def newton(num):
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + num / estimate) / 2
        difference = abs(num - estimate ** 2)
        if difference <= tolerance:
            break
    print("The programs estimate is: " + str(estimate))
    print("Python's estimate: " + str(math.sqrt(num)))

def main():
    val = input("Enter a positive number or press 'Enter' to quit: ")
    if val == "":
        exit()
    else:
        newton(float(val))
        main()

main()