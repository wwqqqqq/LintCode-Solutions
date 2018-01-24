def aplusb(a, b):
    print(a, b)
    if a == 0:
        return b
    elif b == 0:         
        return a
    x = a & 1
    y = b & 1
    print("x, y", x, y)
    if x == 1 and y == 1:
        return ((aplusb(a>>1, b>>1) + 1)<<1)
    elif x == 0 and y == 0:
        return (aplusb(a>>1, b>>1))<<1
    else:
        res = aplusb(a>>1, b>>1)
        print(res, res<<1, res<<1 +1)
        return ((aplusb(a>>1, b>>1))<<1) + 1
    
print(aplusb(100, -100))