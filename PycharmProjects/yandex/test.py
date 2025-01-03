a = []
b = "1"
maxL = 0
while b != "":
    b = input(str())
    if b == "":
        break
    else:
        a.append(b)

for x in range(0, len(a)):
    if len(a[x]) > maxL:
        maxL = len(a[x])


a.reverse()
z = len(a) - 1
x = 0

for x in range(0, 8):
    try:
        while maxL > len(a[x]):
            if len(a[x]) < maxL:
                a[x] = a[x] + "-"
            if len(a[x]) < maxL:
                a[x] = "-" + a[x]
            if len(a[x]) == maxL:
                x += 1
    except:
        print()

for x in range(0, len(a)):
    print(a[x])

