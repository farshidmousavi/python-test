#This is the first answer i did write to solve the problem (or answer the question)
def capital_indexes2(word):
    n = 0
    l = []
    for a in word:
        if a.isupper():
            l.append(n)
        n=n+1
    return l
