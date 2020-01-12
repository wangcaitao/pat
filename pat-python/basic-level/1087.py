n = int(input())

results = set()
for i in range(1, n + 1):
    results.add(int(i / 2) + int(i / 3) + int(i / 5))
else:
    print(len(results))
