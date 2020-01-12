def getPassword(str):
    if str == "A":
        return "1"
    elif str == "B":
        return "2"
    elif str == "C":
        return "3"
    elif str == "D":
        return "4"


n = int(input())

password = ""
for i in range(n):
    inputStr = input()
    if inputStr[2] == "T":
        password += getPassword(inputStr[0])
    elif inputStr[6] == "T":
        password += getPassword(inputStr[4])
    elif inputStr[10] == "T":
        password += getPassword(inputStr[8])
    elif inputStr[14] == "T":
        password += getPassword(inputStr[12])
else:
    print(password)
