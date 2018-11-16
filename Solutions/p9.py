for a in range(1, 998):
    for b in range(a+1, 1000-a):
        c = 1000 - a - b
        if c < a or c < b:
            continue
        else:
            if a**2 + b**2 == c**2:
                print(a*b*c)
