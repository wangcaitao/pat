a, b = [int(value) for value in input().split()]

c = a * b

while c % 10 == 0:
    c //= 10
else:
    print(str(c)[::-1])
