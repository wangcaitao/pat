n, m = [int(value) for value in input().split(" ")]

for i in range(n):
    scores = [int(value) for value in input().split(" ")]

    scoresLen = len(scores)
    maxScore = -1
    minScore = 51
    sum = 0
    count = 0
    for j in range(1, scoresLen, 1):
        if scores[j] > m or scores[j] < 0:
            continue

        if scores[j] < minScore:
            minScore = scores[j]

        if scores[j] > maxScore:
            maxScore = scores[j]

        sum += scores[j]
        count += 1

    print(int(((sum - maxScore - minScore) / (count - 2) + scores[0]) / 2 + 0.5))
