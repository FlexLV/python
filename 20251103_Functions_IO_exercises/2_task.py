def max(a,b,c):
    if a<=b and c<=b:
        return b
    elif a<=c and b<=c:
        return c
    elif b<=a and c<=a:
        return a