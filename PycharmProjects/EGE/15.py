
# не проверенно


for a in range(1000, 1, -1):   # сейчас ищется наибольшее, если надо наименьшее просто, обычный range
    k = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((y + 5 * x != 80) or (3 * x > a) or (y > a)) == False:
                k = False
                break
        if k == False:
            break
    if k == True:
        print(a)
        break




