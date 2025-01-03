count = 0
maxR = -999999
f = open("17.txt")
arr = [int(i) for i in f]
for i in range(len(arr) - 1):
    if (i % 19 == 0) and (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0):
        count += 1
        if i > maxR:
            maxR = i

print(count, maxR)
