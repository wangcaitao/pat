a = input()
b = input()
c = ""

for value in a:
    if value not in c:
        c += value

for value in b:
    if value not in c:
        c += value

print(c)
