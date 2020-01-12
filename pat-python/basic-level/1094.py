import math


def isPrimeNumber(number):
    if number == 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    else:
        return True


l, k = [int(value) for value in input().split()]
n = input()

for i in range(len(n) - k + 1):
    numberStr = n[i:i + k]
    if isPrimeNumber(int(numberStr)):
        print(numberStr)
        break
else:
    print("404")
