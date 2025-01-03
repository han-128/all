for s in range(-10000, 100000):
    n = 1
    while s > 110:
        s = s - 15
        n = n + 4
    if n == 17:
        print(s)