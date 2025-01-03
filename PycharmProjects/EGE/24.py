f = open("24.txt")
st = f.read()
f.close()
cur = 0
maxC = 0
for x in st:
    if x == "C":
        cur += 1
    else:
        cur = 0
    if cur > maxC:
        maxC = cur
print(maxC)
