n = int(input())

maxDistance = 0
minDistance = 0
bestId = ""
worstId = ""

for i in range(n):
    id, x, y = [value for value in input().split()]

    distance = int(x) ** 2 + int(y) ** 2
    if i == 0:
        maxDistance = distance
        worstId = id
    else:
        if distance > maxDistance:
            maxDistance = distance
            worstId = id

    if i == 0:
        minDistance = distance
        bestId = id
    else:
        if distance < minDistance:
            minDistance = distance
            bestId = id
else:
    print(bestId + " " + worstId)
