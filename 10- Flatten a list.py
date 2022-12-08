def flatten(a):
    b=[]
    n=0
    for l in a:
        for s in l:
            b.append(s)
            n=n+1
    return b
