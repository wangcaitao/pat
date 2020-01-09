n, m = [int(value) for value in input().split(" ")]
checkItems = [value for value in input().split(" ")]

totalN = 0
totalM = 0
for i in range(n):
    items = [value for value in input().split(" ")]
    flag = True
    output = ""
    itemLength = len(items)
    for j in range(1, itemLength):
        for k in range(m):
            if items[j] == checkItems[k]:
                if flag:
                    output = output + items[0] + ": "
                    flag = False

                output = output + items[j] + " "
                totalM += 1

    if len(output) > 0:
        totalN += 1
        print(output.rstrip())

print(str(totalN) + " " + str(totalM))
