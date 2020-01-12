n = int(input())

outputArray = []

for i in range(n):
    id, score, school = input().split()

    school = school.lower()

    score = float(score)
    if id[0] == "B":
        score /= 1.5
    elif id[0] == "T":
        score *= 1.5

    for array in outputArray:
        if array[0] == school:
            array[1] += score
            array[2] += 1

            break
    else:
        outputArray.append([school, score, 1])

outputArrayRowLen = len(outputArray)
for i in range(outputArrayRowLen):
    outputArray[i][1] = int(outputArray[i][1])

outputArray.sort(key=lambda value: [-value[1], value[2], value[0]])

print(outputArrayRowLen)
rank = 1
for i in range(outputArrayRowLen):
    if i == 0:
        print(str(rank) + " " + " ".join(str(value) for value in outputArray[i]))
    else:
        if outputArray[i][1] != outputArray[i - 1][1]:
            rank = i + 1

        print(str(rank) + " " + " ".join(str(value) for value in outputArray[i]))
