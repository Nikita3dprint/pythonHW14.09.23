for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z or not y) or x) and (not x or not y) or w) == 0:
                    print(x, y, z, w)
                    