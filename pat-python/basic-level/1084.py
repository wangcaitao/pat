d, n = input().split()

outputStr = d

for i in range(int(n) - 1):
    outputStrLen = len(outputStr)
    if outputStrLen == 1:
        outputStr += "1"
    else:
        tempStr = ""
        count = 1

        for j in range(1, outputStrLen):
            if outputStr[j] == outputStr[j - 1]:
                count += 1

                if j == outputStrLen - 1:
                    tempStr += outputStr[j - 1] + str(count)
            else:
                tempStr += outputStr[j - 1] + str(count)

                if j == outputStrLen - 1:
                    tempStr += outputStr[j] + "1"

                count = 1
        else:
            outputStr = tempStr
else:
    print(outputStr)
