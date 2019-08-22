m, x, y = [int(value) for value in input().split()]


def compare(a, b):
    if a > b:
        return "Cong"
    elif a == b:
        return "Ping"
    else:
        return "Gai"


for first in range(99, 9, -1):
    if first % 10 == 0:
        second = first // 10
    else:
        second = int(str(first)[::-1])

    third = second / y

    if abs(first - second) == third * x:
        print(str(first) + " " + compare(first, m) + " " + compare(second, m) + " " + compare(third, m))

        break
else:
    print("No Solution")
