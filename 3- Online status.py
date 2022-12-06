#After each answer, please share your answer with me
def online_count(a):
    n = 0
    for v in a.values():
        if v == 'online':
            n=n+1
    return n
