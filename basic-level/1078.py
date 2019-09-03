ch = input()
inputStr = input()

outputStr = ""
inputStrLen = len(inputStr)
if 1 == inputStrLen:
    outputStr = inputStr
else:
    if "C" == ch:
        count = 1
        for i in range(1, inputStrLen, 1):
            if inputStr[i] == inputStr[i - 1]:
                count += 1
            else:
                if 1 < count:
                    outputStr += str(count) + inputStr[i - 1]
                else:
                    outputStr += inputStr[i - 1]

                count = 1
        else:
            if 1 < count:
                outputStr += str(count) + inputStr[i]
            else:
                outputStr += inputStr[i]
    elif "D" == ch:
        number = ""
        for i in range(0, inputStrLen, 1):
            if inputStr[i] >= "0" and inputStr[i] <= "9":
                number += inputStr[i]
            else:
                if "" == number:
                    outputStr += inputStr[i]
                else:
                    outputStr += inputStr[i] * int(number)
                    number = ""

print(outputStr)
