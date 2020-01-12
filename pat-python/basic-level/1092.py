n, m = [int(value) for value in input().split()]

totalSalesQuantities = [0] * n
for i in range(m):
    salesQuantities = [int(value) for value in input().split()]
    for j in range(n):
        totalSalesQuantities[j] += salesQuantities[j]

maxTotalSalesQuantity = max(totalSalesQuantities)

maxTotalSalesQuantityIndexes = []
for index, value in enumerate(totalSalesQuantities):
    if value == maxTotalSalesQuantity:
        maxTotalSalesQuantityIndexes.append(index + 1)

print(maxTotalSalesQuantity)
print(" ".join(str(value) for value in maxTotalSalesQuantityIndexes))
