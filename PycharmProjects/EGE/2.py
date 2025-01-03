print("x y z w") # могут быть другие буквы, менять
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = (((z <= x) * (x <= w)) + (y == (z + x))) # вот это менять
                if F == 0: # 0 или 1 по условию?
                    print(x,y,z,w)


