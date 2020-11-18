def binary(primes: list, lower, upper, target): 
    if upper < lower:
        return -1
    guess = int((lower + upper) / 2)
    if primes[guess] == target:
        print(guess)
        return guess
    if primes[guess] > target:
        binary(primes, lower, guess - 1, target)
    else:
        binary(primes, guess + 1, upper, target)


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    lLimit = 0
    uLimit = len(primes) - 1
    target = int(input("Enter a number: "))
    binary(primes, lLimit, uLimit, target)

main()