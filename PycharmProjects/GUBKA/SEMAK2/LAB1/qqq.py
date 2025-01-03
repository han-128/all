ctrok = [0, 1, 2, 3, 4, 5, 6, 7]
stolb = [0, 1, 2, 3, 4, 5, 6, 7]
slon = [1, 1, 2, 3, 4, 5, 6, 7, 8]


XallX = 64

mas = [["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X"]]
for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ')
    print()

print(slon[0])

print()
print()
print()
print()

for s in slon:
    for i in stolb:
        for j in ctrok:
            if (mas[i][j] == "X") and (any([slon[s] in row for row in mas])):
                mas[i][j]  = slon[s]   
            else:
                break

for i in range(0, len(mas)):
    for i2 in range(0, len(mas[i])):
        print(mas[i][i2], end=' ')
    print()