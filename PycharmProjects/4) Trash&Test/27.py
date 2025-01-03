f = open("277.txt")
a = [int(x) for x in f]
f.close()

maxR = 0

for x in range (len(a)):
    if (a[x] * a[x + 1]) % 84 == 0:
        if (a[x] * a[x + 1]) > maxR:
            maxR = (a[x] * a[x + 1])

print(maxR)
        