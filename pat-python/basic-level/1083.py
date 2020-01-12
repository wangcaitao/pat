n = int(input())

inputArray = [int(value) for value in input().split()]
outputArray = [0] * n

for i in range(1, n + 1):
    outputArray[abs(inputArray[i - 1] - i)] += 1

for i in range(n - 1, -1, -1):
    if outputArray[i] > 1:
        print(str(i) + " " + str(outputArray[i]))
