nums = input().split()

successResults = []
for i in range(int(nums[1])):
    successResults.append(input().split())

errors = [[0 for i in range(5)] for i in range(int(nums[1]))]
maxCount = 0
for i in range(int(nums[0])):
    totalScore = 0.0
    studentAllResults = input()[1:-1].split(") (")
    for j, studentResult in enumerate(studentAllResults):
        studentResults = studentResult.split()
        count = 0
        flag = True
        for k in range(int(successResults[j][1])):
            result = chr(k + 97)
            if result in successResults[j][3:] and result in studentResults[1:]:
                count += 1
            elif result in successResults[j][3:] and result not in studentResults[1:]:
                errors[j][k] += 1
            elif result not in successResults[j][3:] and result in studentResults[1:]:
                errors[j][k] += 1
                flag = False

            if errors[j][k] > maxCount:
                maxCount = errors[j][k]

        if flag:
            if count == int(successResults[j][2]):
                totalScore += float(successResults[j][0])
            else:
                totalScore += float(successResults[j][0]) / 2

    print("{:.1f}".format(totalScore))

if maxCount:
    for i, error in enumerate(errors):
        for j, count in enumerate(error):
            if count == maxCount:
                print("{} {}-{}".format(maxCount, i + 1, chr(j + 97)))
else:
    print("Too simple")
