for x in range(70, 1000000):
    L = x
    M = 71
    if L % 2 != 0:
        M = 42
    while L != M:
        if L > M:
            L -= M
        else:
            M -= L
    if M == 21:
        print(x)
