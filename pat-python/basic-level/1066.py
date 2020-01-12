inputParams = input().split()

for i in range(int(inputParams[0])):
    grayValues = input().split()
    n = int(inputParams[1])
    for j in range(n):
        if int(grayValues[j]) >= int(inputParams[2]) and int(grayValues[j]) <= int(inputParams[3]):
            grayValues[j] = inputParams[4]

        if j == n - 1:
            print("{:0>3s}".format(grayValues[j]))
        else:
            print("{:0>3s} ".format(grayValues[j]), end="")
