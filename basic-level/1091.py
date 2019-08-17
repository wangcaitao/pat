m = int(input())
numbers = [int(value) for value in input().split()]

for i in range(m):
    number = numbers[i]
    for j in range(10):
        anotherNumber = j * pow(number, 2)
        if str(anotherNumber).endswith(str(number)):
            print("{} {}".format(j, anotherNumber))
            break
    else:
        print("No")
