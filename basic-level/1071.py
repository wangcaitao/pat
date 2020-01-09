total, k = [int(value) for value in input().split(" ")]


for i in range(k):
    if total <= 0:
        print("Game Over.")
        break

    n1, b, t, n2 = [int(value) for value in input().split(" ")]

    if t > total:
        print("Not enough tokens.  Total = " + str(total) + ".")
    else:
        if n2 < n1:
            if b == 0:
                total += t
                print("Win " + str(t) + "!  Total = " + str(total) + ".")
            else:
                total -= t
                print("Lose " + str(t) + ".  Total = " + str(total) + ".")
        else:
            if b == 0:
                total -= t
                print("Lose " + str(t) + ".  Total = " + str(total) + ".")
            else:
                total += t
                print("Win " + str(t) + "!  Total = " + str(total) + ".")
