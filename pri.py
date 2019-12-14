def prime(s=int,e=int):
    for p in range(s, e+1):
        if p > 1:
            for n in range(2, p):
                if (p % n) == 0:
                    break
            else:
                print(p)
