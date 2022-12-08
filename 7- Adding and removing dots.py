def add_dots(a):
    l = ''
    for i in a:
        l=l+(i+".")
    return l[:-1]
    
def remove_dots(b):
    return b.replace('.','')
